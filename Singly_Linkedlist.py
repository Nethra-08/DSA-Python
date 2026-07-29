class Song:
    def __init__(self,data):
        self.data=data
        self.next=None
class Playlist():
    def __init__(self):
        self.head=None
    def append(self,data):
        new_song=Song(data)
        if self.head is None:
            self.head=new_song
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_song
    def prepand(self,data):
        new_song=Song(data)
        new_song.next=self.head
        self.head=new_song
    def insert_at_position(self, data, pos):
        new_song = Song(data)

        if pos == 0:
            new_song.next = self.head
            self.head = new_song
            return

        current = self.head
        count = 0

        while current and count < pos - 1:
            current = current.next
            count += 1

        if current is None:
            print("Invalid position")
            return

        new_song.next = current.next
        current.next = new_song

    
    def delete(self,data):
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head,next
            return
        current=self.head
        while current.next:
            if current.next.data==data:
                current.next=current.next.next
                return
        current=current.next
    def display(self):
        current=self.head
        while current:
            print(current.data,end="-->")
            current=current.next
        print("None")


play_list=Playlist()
play_list.append("Nallaru Po...")
play_list.append("Kanana kanne ne kalangathadii!!")
play_list.prepand("Karupuuu !")
play_list.prepand("Mannichiru")
play_list.display()
play_list.insert_at_position("Hukum", 2)
play_list.display()
play_list.delete("Mannichiru")
