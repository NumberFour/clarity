$LOAD_PATH.unshift File.join(File.dirname(__FILE__), "lib")

require 'rubygems'
gem 'hoe', '>= 2.1.0'
gem 'newgem'

require 'hoe'
require 'clarity'

Hoe.plugin :newgem

$hoe = Hoe.spec 'numberfour-clarity' do
  self.developer 'Tobias Lütke', 'tobi@shopify.com'
  self.developer 'John Tajima', 'john@shopify.com'
  self.developer 'Jens Bräuer', 'braeuer.jens@googlemail.com'
  self.summary = 'Web interface for grep and tail -f'  
  self.post_install_message = 'PostInstall.txt'  
  self.readme_file          = 'README.rdoc'  
  self.extra_deps           = [['eventmachine','>= 0.12.10'], ['eventmachine_httpserver','>= 0.2.0'], ["json", ">= 1.0.0"], ["log4j", '>= 1.1.19']]
  self.test_globs           = ['test/**/*_test.rb']
end

require 'newgem/tasks'
Dir['tasks/**/*.rake'].each { |t| load t }