info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
my_str = info.split(':').join('+')
puts my_str