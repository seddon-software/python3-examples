from pysnmp.entity.rfc3413.oneliner import ntforg
from pysnmp.proto import rfc1902

ntfOrg = ntforg.NotificationOriginator()

ntfOrg.sendNotification(
    ntforg.CommunityData('public'),
    ntforg.UdpTransportTarget(('localhost', 162)),
    'trap',
    ntforg.MibVariable('SNMPv2-MIB', 'coldStart'),
    ('1.3.6.1.2.1.1.1.0', rfc1902.OctetString('my system'))
)
