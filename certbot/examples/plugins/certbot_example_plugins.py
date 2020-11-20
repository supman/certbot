"""Example Certbot plugins.

For full examples, see `certbot.plugins`.

"""
import zope.interface

from certbot import interfaces
from certbot.plugins import common
from certbot.plugins import dns_common


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

    def more_info(self):  # pylint: disable=missing-docstring,no-self-use
        return (
            "This plugin configures a DNS CNAME record to respond to a dns-01 challenge using "
            + "the EuroDNS Remote REST API."
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
