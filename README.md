# A script to convert annotated NER dataset in XML format to CoNLL format or sentenced format for several usage

For Named Entity Recognition (NER) task, several formats of datasets are used, such as CoNLL, ENAMEX tagging etc.
In order to use and inspect datasets several libraries (Pandas, Scikit Learn, etc.) provide flexible usage.
However these libraries need a bit structured data. Therefore, CoNLL and Sentenced data formats are needed.
Followings are brief descriptions of the formats:

## XML
In XML format, our file will be in the below format, where IOB2 tags are in a block.
Each line is a sentence. Words are in raw format, i.e. not tokenized.
```
<doc>
    <tag1>New York</tag1> is a city.
    Hello, there!
</doc>
```

## CoNLL
In this format, each word presented with its tag, and sentences are separated with an empty line. 
Words and tags are separated with a space.
```
New   B-LOC
York  I-LOC
is    O
a     O
city  O
.     O

Hello O
,     O
there O
!     O
```

## Sentenced
In this format each word is presented with its tag and sentence number, all separated with tab.
```
sentence_no   word        tag
Sentence: 1   New         B-LOC
Sentence: 1   York        I-LOC
Sentence: 1   is          O
Sentence: 1   a           O
Sentence: 1   beautiful   O
Sentence: 1   city        O
Sentence: 2   Hello       O
Sentence: 2   ,           O
Sentence: 2   there       O
Sentence: 2   !           O
```

