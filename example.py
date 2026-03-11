from interpreter import PitonetonInterpreter

interpreter = PitonetonInterpreter()

# Variable assignment with arithmetic
interpreter.execute('let x = 10')
interpreter.execute('let y = x + 5')

# Print variables and expressions
interpreter.execute('print x')
interpreter.execute('print y')
interpreter.execute('print x * y')

# If condition
interpreter.execute('if x > 5 then print "x is greater than 5"')
interpreter.execute('if x < 5 then print "x is less than 5"')