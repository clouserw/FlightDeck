var Class = require('shipyard/class/Class'),
	Model = require('shipyard/model/Model'),
	fields = require('shipyard/model/fields'),
	Syncable = require('shipyard/sync/Syncable'),
	ServerSync = require('shipyard/sync/Server');

var Package = module.exports = new Class({

	Extends: Model,

	Implements: Syncable,

	Sync: {
		'default': {
			driver: ServerSync,
			route: '/api/0/packages'
		}
	},

	//pk: 'id_number',

	fields: {
		id: fields.NumberField(),
		id_number: fields.NumberField(), // the real PK?
		full_name: fields.TextField(),
		name: fields.TextField(),
		description: fields.TextField(),
		type: fields.TextField(), //ChoiceField({ choices: ['a', 'l'] })
		author: fields.TextField(),
		url: fields.TextField(),
		license: fields.TextField(),
		version_name: fields.TextField(),
		revision_number: fields.NumberField(),

        latest: fields.NumberField(), // a FK to PackageRevision

		// modules: FK from Module
		// attachments: FK from Attachment
		// dependencies: ManyToManyField('self')
	},

    isAddon: function isAddon() {
        return this.get('type') === this.constructor.TYPE_ADDON;
    },

    isLibrary: function isLibrary() {
        return this.get('type') === this.constructor.TYPE_LIBRARY;
    },

	toString: function() {
		return this.get('full_name');
	}

});

Package.TYPE_ADDON = 'a';
Package.TYPE_LIBRARY = 'l';
