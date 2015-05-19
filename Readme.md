# Rover Lapse Bot

Runs every 4 hours. Pulls the images from eathroverbot, filters out duplicate images, condenses the images a bit, then uses the images2gif library to generate an animated gif.

I’m not super happy with the quality of images, but Twitter has an image size limit of ~3 megs and if I left the images at 600x600px I would only get about 10 in the animation – crunching down to 350 lets me put 25 in there, but it looks kind of bad since the twitter gif viewer stretches the images to fit a standard size when it plays them.

I recently started a job where I work in Python all day and do a lot of unit testing, so this is the first bot I’ve made that is moderately well-tested. (I got slack towards the end when the finish line was in sight.)
