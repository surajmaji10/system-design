
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
        {duration: '10s', target: 1000},
        {duration: '20s', target: 1000},
        {duration: '30s', target: 0}
    ]
};



export default function(){
    let resp = http.get("http://localhost:9090/load");

    check(resp, {
        "is response 200": (r) => r.status === 200
    });

    sleep(0.5);
}

