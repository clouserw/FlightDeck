import os

from commander.deploy import hostgroups, task


AMO_PYTHON_ROOT = '/data/amo_python'
FLIGHTDECK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


@task
def deploy_code(ctx):
    with ctx.lcd(AMO_PYTHON_ROOT):
        ctx.local("/usr/bin/rsync -aq --exclude '.git*' --delete src/builder/ www/builder/")
        with ctx.lcd("www"):
            ctx.local("git add .")
            ctx.local("git commit -a -m 'flightdeck push'")

    pull_code()


@hostgroups(["amo", "amo_gearman"])
def pull_code(ctx):
    ctx.remote("/data/bin/libget/get-php5-www-git.sh")
    ctx.remote("touch /data/amo_python/www/builder/flightdeck/wsgi/flightdeck.wsgi")


@hostgroups(["amo_gearman"])
def restart_celery(ctx):
    ctx.remote("service celeryd-builder_prod restart")
    ctx.remote("service celeryd-builder_prod_bulk restart")


@task
def schematic(ctx):
    with ctx.lcd(FLIGHTDECK_DIR):
        ctx.local("python2.6 ./vendor/src/schematic/schematic migrations")


def _git_checkout_tag(ctx, tag):
    ctx.local("git fetch -t origin")
    ctx.local("git checkout %s" % tag)
    ctx.local("git submodule sync")
    ctx.local("git submodule update --init --recursive")


@task
def start_update(ctx, tag):
    """Updates code to `tag`"""
    with ctx.lcd(FLIGHTDECK_DIR):
        _git_checkout_tag(ctx, tag)


@task
def update_flightdeck(ctx):
    """Deploys code to the webservers and restarts celery"""
    schematic()
    deploy_code()
    restart_celery()
