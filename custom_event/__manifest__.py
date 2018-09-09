# -*- coding: utf-8 -*-
{
    'name': 'Custom Event',
    'version': '1.0',
    'category': 'Marketing',
    'summary': 'Trainings, Conferences, Meetings, Exhibitions, Registrations',
    'description': """
Organization and management of Events.
======================================

The event module allows you to efficiently organize events and all related tasks: planning, registration tracking,
attendances, etc.

Key Features
------------
* Manage your Events and Registrations
* Use emails to automatically confirm and send acknowledgments for any event registration
""",
    'depends': ['base', 'event'],
    'data': [
        'views/event_view.xml',
    ],
    'application':True,
    'installable': True,
    'auto_install': False,
}
