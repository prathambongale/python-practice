spam_amount = 0 # valiable assignment - assigning value 0 to spam_amount using =, which is assignment operator 
# No need to declare varibale before assignment like Java or C++.
# No need to define datatype for varibale. Varibale can store any value.

print(spam_amount) # use to display value on console that is pass to it

spam_amount = spam_amount + 4   # reassignment of value

if spam_amount > 0:
    print("But I don't wamt AMY spam!")

viking_song = "Spam " * spam_amount
print(viking_song) # This will print "Spam Spam Spam Spam"


viking_song = 4 * spam_amount
print(viking_song) # This will print "16"

# operators like * and + have a different meaning depending on what kind of thing they're applied to. (The technical term for this is operator overloading)