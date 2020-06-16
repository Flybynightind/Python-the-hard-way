my_name = 'Zed A. Shaw'
my_age = 41 #not a lie
my_height = 78 #inches
my_weight = 240 #lbs
my_eyes = 'hazel'
my_teeth = 'White'
my_hair = 'Brown'
my_weight_in_kilos = my_weight * .453
my_height_in_cms = my_height * 2.54


print "Let's talk about %s." % my_name
print "He'd %d cms tall." % my_height_in_cms
print "He's %d kilos heavy." % my_weight_in_kilos
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

