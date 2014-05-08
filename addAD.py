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
 
    dn = "CN=testaccount,OU=office,DC=test,DC=com"
    attrs = {}
    attrs['objectclass'] = 
    attrs['cn'] = 'testaccount'
    attrs['sAMAccountName'] = 'testaccount'
    attrs['description'] = 'Just for test'
    
    ldif = modlist.addModlist(attrs)
    l.unbind_s() 
except ldap.LDAPError as e:
    print e
