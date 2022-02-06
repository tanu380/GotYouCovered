# GotYouCovered
This bot celebrates women by not letting people post images that are unsafe for work. These images include nude images that are very demeaning to the society and makes women uncomfortable. This helps the bot not only to prevent people from sending demeaning pictures of women, but also helps women avoid the distress that they feel in everyday life because of these pictures.

We have not uploaded the config file because of token secrecy issues, the code for the discord bot "GotYouCovered" is in main.py
## Inspiration
We live in a world where it is really difficult to go out and interact with people because of covid. Internet is the only resort. But as we all know, it is really not such a happy place for everyone. People have found ways of harassing others, especially women on the internet. They post obscene content of women and themselves on the internet on various sites, creating an unhealthy and unethical platform. It makes women uncomfortable and after digging deeper into it, we found out that uncomfortable is just a small term; this type of incongruous content negatively impacts women's mental health which is the root cause of various further illnesses like depression, anxiety, and much more. This gave us the motivation to do our part and help women fight and stand against such behavior. This is how we came up with our discord bot "GotYouCovered". This bot helps us celebrate women in tech, makes it a safe haven for them, and prevents any unsuitable content like naked pictures and similar content having the power to affect their health, from being posted.
## What it does
Our discord bot "GotYouCovered" first checks if the message has an attachment or not. If it does, it sends the image attachment through a neural network classifier. This classifier gives us a safe and an unsafe score. This unsafe score helps the bot decides if an image should be deleted or not. If the unsafe score is higher, the bot deletes it. The bot also kicks a user out of the discord server if they have sent inappropriate content more than 3 times. Hence, our discord bot plays its part in making the discord community a better and safe place for women to interact and learn. This also helps women attain mental stability because they know, "GotYouCovered" has got them covered from inappropriate content.
## How we built it
We built our bot in python using the discord.py library and nudeNEt model. Our bot checks for an attachment in the message and sends it through a neural network classifier model. This neural network classifier is a pre-trained classifier trained on more than 160,000 images. The nudeNet model gives us a safe and unsafe score which decides if the image is improper. If classified as an unsafe image, our code increments the counter for that specific user, and if they have sent inappropriate content more than 3 times, the bot kicks that user out of the server. 
## Challenges we ran into
We learned how to use the neural network in our code and learned how that specific neural network works. This was the first time for us dealing with something related to deep learning and we struggled a bit towards the beginning trying to understand the code, but towards the end of it, we are proud that we understood it and used it to fight against the evil, towards a better community for women free of hate and demeaning content.
## Accomplishments that we're proud of
We are proud that being in our first-ever hackathon, we were able to deliver a project that successfully goes along with the aim of celebrating women and making a safer community. We are proud to announce that our bot successfully classifies and deletes unsafe images from the discord server, helping women achieve mental health stability, making people aware, and being a small part of a big cause.
## What we learned
Both of us didn't come with a team of our own to our first hackathon ever. But what we learned is teamwork, we learned that we don't have to know each other to work together, we just have to have the will to learn. Working with an absolute stranger, I learned how to work as a team, bouncing ideas out of each others' heads and thinking together towards a solution, one step at a time.
## What's next for GotYouCovered
We plan to improve our bot and upgrade it to classify videos as safe and unsafe. We also plan to work on a solution towards darkening/blurring the areas of the image/video in real time. We plan that our bot detects hate in the form of speech and text and we are positive that we will be able to do it.
