import { Component, OnInit } from '@angular/core';
import * as firebase from 'firebase/app';
import 'firebase/firestore';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'Kool';
  likes: number ;
  username: number ;
  participants: any[]=[];
  ngOnInit(){
    this.getParticipants();  
  }
  getParticipants(){
    this.participants=[];
   firebase.firestore().collection("participants")
   .orderBy("likes","desc")
   .orderBy("time","desc")
   .get()
   .then((data)=>{
    data.docs.forEach((participantRef)=>{
      this.participants.push(participantRef.data())
      
   })

  })
  }
}
