resource "linode_domain" "domain" {
  domain	= var.domain
  soa_email	= var.soa_email
  type		= "master"
}

resource "linode_domain_record" "domain" {
  domain_id	= linode_domain.domain.id
  name		= var.subdomain
  record_type	= "AAAA"
  target	= linode_instance.server.ip_address
}
