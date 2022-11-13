# srt_cleaner


## Requires Python 3.6+

## Usage
Place in top directory of media files, and run with `python srt_clean.py`. 
It will go through each subdirectory and remove all ads from the files, saving the OG as .original and rewriting the 
.srt files.

Ads to remove can be added in the helpers.offending_lines method. Any match to the lines in the list 
(note it is case-sensitive) will remove that entire section. 

example: if `www.OpenSubtitles` is added to the offending_lines list, then:
```
31
00:01:17,494 --> 00:01:18,579
No!

32
00:01:20,000 --> 00:01:26,074
Support us and become VIP member 
to remove all ads from www.OpenSubtitles.org

33
00:01:38,640 --> 00:01:39,891
Attention, squad.

```
will remove the 
```
32
00:01:20,000 --> 00:01:26,074
Support us and become VIP member 
to remove all ads from www.OpenSubtitles.org

```
and each subsequent section will be updated to be the correct sub line, so the original 33, will become 32 (and so on)

```
31
00:01:17,494 --> 00:01:18,579
No!

32
00:01:38,640 --> 00:01:39,891
Attention, squad.
```
