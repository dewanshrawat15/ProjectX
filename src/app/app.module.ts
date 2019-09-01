import { BrowserModule } from '@angular/platform-browser';
import { NgModule} from '@angular/core';
import { AngularFireModule } from 'angularfire2';  
import { AngularFirestoreModule } from 'angularfire2/firestore'; 
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import * as firebase from 'firebase/app';
import 'firebase/firestore';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CapitalPipe } from './capital.pipe';
import { MenuComponent } from './menu/menu.component';
//npm install -g firebase-tools
const firebaseConfig = {
  apiKey: "AIzaSyAr4AXpaMtS5kZ2Zy0I28gKW7fdWcEqXms",
  authDomain: "leaderboard-b6fc6.firebaseapp.com",
  databaseURL: "https://leaderboard-b6fc6.firebaseio.com",
  projectId: "leaderboard-b6fc6",
  storageBucket: "",
  messagingSenderId: "741983237165",
  appId: "1:741983237165:web:ce413bf121f0c7cf"
};
firebase.initializeApp(firebaseConfig)
@NgModule({
  declarations: [
    AppComponent,
    CapitalPipe,
    MenuComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    AngularFireModule,
    AngularFirestoreModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
