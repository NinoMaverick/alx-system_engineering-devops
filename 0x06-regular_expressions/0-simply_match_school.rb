#!/usr/bin/env ruby
# Ensure an argument is provided
if ARGV.empty?
    puts "Please provide an argument."
    exit
  end
  
  # Extract the argument
  input_string = ARGV[0]
  
  # Define the regular expression pattern
  pattern = /School/
  
  # Check if the input matches the pattern
  if input_string.match?(pattern)
    puts "The input '#{input_string}' contains the word 'School'."
  else
    puts "The input '#{input_string}' does not contain the word 'School'."
  end
  
