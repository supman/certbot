"""Example Certbot plugins.

For full examples, see `certbot.plugins`.

"""

import logging

import zope.interface

from certbot import interfaces
from certbot.plugins import common
from certbot.plugins import dns_common

logger = logging.getLogger(__name__)

ACCOUNT_URL = 'https://docapi.eurodns.com/dns'

@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)
class Authenticator(dns_common.DNSAuthenticator):
    """Example Authenticator for EuroDNS."""

    description = "Example Authenticator plugin for EuroDNS"

    # Implement all methods from IAuthenticator, remembering to add
    # "self" as first argument, e.g. def prepare(self)...
    def __init__(self, *args, **kwargs):
        super(Authenticator, self).__init__(*args, **kwargs)
        self.credentials = None

    @classmethod
    def add_parser_arguments(cls, add):  # pylint: disable=arguments-differ
        super(Authenticator, cls).add_parser_arguments(add, default_propagation_seconds=30)
        add(
            "credentials",
            help="EuroDNS credentials INI file.",
            default="/etc/letsencrypt/eurodns.ini",
        )

    def more_info(self):  # pylint: disable=missing-docstring,no-self-use
        return (
            "This plugin configures a DNS CNAME record to respond to a dns-01 challenge using "
            + "the EuroDNS Remote REST API."
        )

    def _setup_credentials(self):
        self.credentials = self._configure_credentials(
            'credentials',
            'EuroDNS credentials INI file',
            {
                'token': 'User access token for DNSimple v2 API. (See {0}.)'.format(ACCOUNT_URL)
            }
        )

    def _perform(self, domain, validation_name, validation):
        return (
            "This plugin configures a DNS CNAME record to respond to a dns-01 challenge using "
            + "the EuroDNS Remote REST API."
        )

    def _cleanup(self, domain, validation_name, validation):
        return (
            "This plugin configures a DNS CNAME record to respond to a dns-01 challenge using "
            + "the EuroDNS Remote REST API."
        )

@zope.interface.implementer(interfaces.IInstaller)
@zope.interface.provider(interfaces.IPluginFactory)
class Installer(common.Plugin):
    """Example Installer."""

    description = "Example Installer plugin"

    # Implement all methods from IInstaller, remembering to add
    # "self" as first argument, e.g. def get_all_names(self)...
