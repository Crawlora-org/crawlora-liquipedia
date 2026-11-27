require_relative "lib/crawlora/liquipedia/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-liquipedia"
  spec.version = Crawlora::Liquipedia::VERSION
  spec.summary = "Liquipedia API client for Crawlora (14 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted Liquipedia API. Covers wiki discovery, pages, search, categories, recent changes, links, and backlinks across 14 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=liquipedia-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-liquipedia", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-liquipedia/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
