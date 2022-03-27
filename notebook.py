# Code was taken from the second edition of 
# Python 3 Object-oriented Programming by Dusty Phillips
from note import Note

class Notebook:
    '''Represent a collection of notes that can be tagged,
    modified, and searched.'''
    def __init__(self):
        '''Initialize a notebook with an empty list.'''
        self.notes = []
        
    def new_note(self, memo, tags=''):
        '''Create a new note and add it to the list.'''
        self.notes.append(Note(memo, tags))
        
    def modify_memo(self, note_id, memo):
        '''Find the note with the given id and change its
         memo to the given value.'''
         note = self._find_note(note_id)
         if note:
             note.memo = memo
             return True
         return False
                
    def modify_tags(self, note_id, tags):
        '''Find the note with the given id and change its
        memo to the given value.'''
        note = self._find_note(note_id)
         if note:
             note.tags = tags
             return True
         return False
        
    def search(self, filter):
        '''Find all notes that match the given filter
        string.'''
        return [note for note in self.notes if
        note.match(filter)]
      
    def _find_note(self, note_id):
        '''Locate the note with the given id.'''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None
    
