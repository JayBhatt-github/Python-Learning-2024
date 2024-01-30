import random 

# comp    user
#  s        g   --> user
#  g        s   --> comp
#  w        s   --> user
#  s        w   --> comp
#  g        w   --> user
#  w        g   --> comp


# 1 --> snake
# 2 --> water
# 3 --> gun

opt = ['1','2','3']

u = input("enter choice snake(1), water(2), gun(3)")
c = random.choice(opt)

if u == '1' and c == '3':
    print("computer choose gun and you lost")
elif u == '2' and c == '3':
    print("computer choose gun and you won")
elif u == '3' and c == '3':
    print("computer choose gun match tied")
    
elif u == '1' and c == '2':
    print("computer choose water and you won")
elif u == '3' and c == '2':
    print("computer choose water and you lost")
elif u == '2' and c == '2':
    print("computer choose water match tied")
    
elif u == '1' and c == '1':
    print("computer choose snake match tied")
elif u == '3' and c == '1':
    print("computer choose snake and you won")
elif u == '2' and c == '1':
    print("computer choose snake and you lost")
    
    








