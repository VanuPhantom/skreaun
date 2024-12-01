resource "linode_instance" "server" {
  label		= "Skreaun"
  region	= "nl-ams"
  type		= "g6-nanode-1"
}
