import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';



@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {
  public text = '';
  constructor(private http: HttpClient) {}
  
  test(mess,lang){
    let showtext = {};
    console.log(mess,lang[0]);
    let header = new Headers()
   this.http
            .post(' http://192.168.0.21:5000/',{
               body: {
                  data: mess,
                  dest: lang[0]
               }
            })
            .subscribe(
              data => {
                //console.log(data);
                showtext=data
                console.log(showtext);
                this.text = JSON.stringify(showtext) 
              },
              error => {
                console.log(error)
              } 
            )
  }

}
