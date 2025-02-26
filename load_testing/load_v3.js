/**
 *  @author: Akash Maji
 *  @email: akashmaji@iisc.ac.in
*/

import http from 'k6/http';
import {sleep, check } from 'k6';

export let options = {
    // duration: '30s',
    // vus: 20

    stages:[
        {duration: '1s', target: 1000},
        {duration: '2s', target: 1000},
        {duration: '3s', target: 0}
    ],

    thresholds:{
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<700'] //in ms
    }
};



export default function(){
    let resp = http.get("http://localhost:9090/load");

    check(resp, {
        "is response 200": (r) => r.status === 200
    });

    sleep(0.5);
}

