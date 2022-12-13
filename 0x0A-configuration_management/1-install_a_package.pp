# This Puppet manifest installs puppet-lint

package { 'flask':
  ensure   => '2.1.0',
  provider => 'gem',
 
}
