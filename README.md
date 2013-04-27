<h1> MIT-shootings Twitter Bot </h1>

<h2> Blog post </h2>

I blogged the process in <a href="https://passionfordata.wordpress.com/2013/04/20/visualising-mitshooting-related-tweets/"> Passion for Data blog</a>. There are also the word cloud images.
<h2> Background </h2>

As MIT shootings started at 18th April 2013, I hacked a quick Twitter bot to keep track of hashtag #mitshooting. After 10 hours, I wordclouded the data.

<h2> Features </h2>

<i>mit.py</i>
Every 15 seconds, the script fetches 15 tweets containing the hashtag #mitshooting and records the tweet and the username to database

<i>analyse-mit.py</i>
The script fetches the tweets from the database and does cleaning (ignores couple of known spams), removes stopwords listed in <i>stopwords.txt</i>, removes punctuation, hashtags, mentions and links.

The script also creates hourly frequency files as well as combined frequency file for the entire 10 hours.

<i>cloud_mit.r</i>
Read the frequency table and uses wordcloud library to create nice looking word clouds.

<i>hourly_cloud.r</i>
Reads one frequency file per hour and creates corresponding word cloud


<h2> Contact </h2>

If you have any ideas to improve the code, feel free to fork and make a pull request to contribute. Or you can contact me via Twitter @hamatti.

<h2> Licence </h2>

Copyright (C) 2013 Juha-Matti Santala

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
