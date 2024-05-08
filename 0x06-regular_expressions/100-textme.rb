#!/usr/bin/env ruby
matches = ARGV[0].scan(/\[from:([a-zA-Z0-9+]+)\]\s*\[to:([a-zA-Z0-9+]+)\]\s*\[flags:(.+?)\])
puts matches.map { |match| match.join(',') }
