from nose.tools import *
from ex49 import sentence
from ex49.sentence import ParserError
from ex49.sentence import Sentence

def test_peek():
    word_list = [('noun', 'princess'), ('verb', 'go'), ('direction', 'left')]
    assert_equal(sentence.peek(word_list), 'noun')

def test_peek_empty():
    empty_word_list = []
    assert_equal(sentence.peek(empty_word_list), None)

def test_match():
    word_list = [('noun', 'princess'), ('verb', 'go'), ('direction', 'left')]
    assert_equal(sentence.match(word_list, 'noun'), ('noun', 'princess'))

def test_match_not_equal():
    word_list = [('noun', 'princess'), ('verb', 'go'), ('direction', 'left')]
    assert_equal(sentence.match(word_list, 'verb'), None)

def test_match_empty():
    empty_word_list = []
    assert_equal(sentence.match(empty_word_list, 'noun'), None)

def test_skip():
    word_list = [('stop', 'the'),
                 ('verb', 'go'),
                 ('direction', 'left')]
    sentence.skip(word_list, 'stop')
    assert_equal(word_list, [('verb', 'go'), ('direction', 'left')])

def test_parse_verb():
    word_list = [('stop', 'the'),
                 ('verb', 'go'),
                 ('direction', 'left')]
    assert_equal(sentence.parse_verb(word_list), ('verb', 'go'))

def test_parse_verb_exception():
    word_list = [('stop', 'the'),
                 ('noun', 'princess'),
                 ('verb', 'go'),
                 ('direction', 'left')]
    assert_raises(ParserError, sentence.parse_verb, word_list)

def test_parse_object_noun():
    word_list = [('stop', 'the'),
                 ('noun', 'princess')]
    assert_equal(sentence.parse_object(word_list), ('noun', 'princess'))

def test_parse_object_direction():
    word_list = [('stop', 'the'),
                 ('direction', 'left')]
    assert_equal(sentence.parse_object(word_list), ('direction', 'left'))

def test_parse_object_exception():
    word_list = [('stop', 'the'),
                 ('verb', 'go')]
    assert_raises(ParserError, sentence.parse_object, word_list)

def test_parse_subject():
    subject = ('noun', 'princess')
    verb = ('verb', 'go')
    obj = ('direction', 'left')
    word_list = [verb, obj]
    s1 = sentence.parse_subject(word_list, subject)
    s2 = Sentence(subject, verb, obj)
    assert_equal(s1.subject, s2.subject)
    assert_equal(s1.verb, s2.verb)
    assert_equal(s1.object, s2.object)

def test_parse_sentence():
    subject = ('noun', 'princess')
    verb = ('verb', 'go')
    obj = ('direction', 'left')
    w1 = [verb, object]
    word_list = [('stop', 'the'),
                 ('noun', 'princess'),
                 ('verb', 'go'),
                 ('direction', 'left')]
    s1 = sentence.parse_sentence(word_list)
    s2 = Sentence(subject, verb, obj)
    assert_equal(s1.subject, s2.subject)
    assert_equal(s1.verb, s2.verb)
    assert_equal(s1.object, s2.object)
