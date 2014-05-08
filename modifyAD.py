import ldap
import ldap.modlist as modlist 

server = ''
sysadmin = ''
password = ''
l = ldap.initialize("ldap://%s", server)
try:
    l.protocol_version = ldap.VERSION3
    l.set_option(ldap.OPT_REFERRALS, 0)
 
    l.simple_bind_s(sysadmin, password)
 
    basedn = "dc=test, dc=com"
    scope = ldap.SCOPE_SUBTREE
    filter  = "(&(objectClass=user)(sAMAccountName=testaccount))"
    attributes = None
    result = l.search_s(basedn, scope, filter, attributes)
    #ls = result[0][1]['physicalDeliveryOfficeName']
    dn = result[0][0]
    old = {'physicalDeliveryOfficeName': ''}
    new = {'physicalDeliveryOfficeName': 'just a test'}
    ldif = modlist.modifyModlist(old, new)
    l.modify_s(dn, ldif)
except ldap.LDAPError as e:
    print e
