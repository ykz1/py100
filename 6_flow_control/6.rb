def all_caps(string)
  return string.length > 10 ? string.upcase : string
end

puts all_caps('hello world')
puts all_caps('goodbye')