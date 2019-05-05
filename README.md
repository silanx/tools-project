## Tools for Analytics-A Tool to Grading Songs

Silan Xu       sx2237

Wanzhen Jiang  wj2289

## What it is?

This **tool** is developed to give flexible and proper scores to a song based on the contents of its lyrics quickly and precisely. After the song is analyzed and scores are given, it would be convenient for users to determine whether it is suitable for specific occasions. For example. it can effectively reduce the change of playing an inappropriate song at a kingdergarten. It is developed to produce a practical, real world data analyzing tool based on Python. In this specific project, we have utilized a lyric bank to figure out whether it is working accurately towards its goal.

## Main Features
Here are the main dimensions this tool can test and their grading methodology:

* Kid_safe
  - It tests whether a specific song contains bad words checked by a profanity library. The more bad words a song contains compared to its own length, the lower grade will be given. For each 1% of more bad word it contains , the score will be decucted by 0.2 points.
  - 0 means it is not kid safe
  - 1 menas it is very kid safe

* Love
  - It tests whether a song is a love song or not, checked by a romantic word library. The more romantic words a song has, the higher grade will be given. The score will go up by 0.1 if the proportion of romantic words compared to the song length goes up by 1%.
  - 0 means it is not a love song
  - 1 means it is a love song

* Mood 
  - It tests whether a song delivers a positive message. The lyrics are checked by two library: a positive and a negative word library. The more positive words the song hits compared to negative words, the score will shift more towards positive. If the song expresses neutral mood, the score will be 0.5. For each 1% of more positive words it hits, the score will go up by 0.3 points, and vice versa.
  - Score > 0.5 means it is positive 
  - Score < 0.5 means it is negative
  - The score range is from 0 to 1

* Length
  - It tests how long is the song. This tool first counts the number of words in all songs to get the average length and compare each song's length to the average. If the length of the song is equal to the average length, its score will be 0.5. If the length is greater than the average, it compares the excess length to the average length. For each 1% excess to the average, the score will be deducted by 0.25 points, and vice versa. 
  - 0 means it is a very short song
  - 1 means it is a very long song
  
* Complexity
  - It tests whether this song requires higher level of vocabulary to understand. It counts how many times the word with the highest frequency appears and compare it with the number of unique words a song contains. The score will be deducted by 0.01 if this ratio goes up by 1%.
  - 0 means it is a very simple song
  - 1 means it is a very complex song

## Expected Output

The output of the program will have the following form:
{
		“characterizations”: [
			{
             			“id”: 45,
				“artist”: “Michael Jackson”,
				“title”: “Billie Jean”,
				“kid_safe”: 0.2,
				“love”: 0.5,
				“mood”: 0.3,
				“length”: 0.3,
				“complexity”: 0.3,
},
			{
				“title”: “Wheels on the bus”,
                                 		....
}
		]
	}

