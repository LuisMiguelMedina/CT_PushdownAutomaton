import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})

export class HttpService {

  private baseUrl = 'http://localhost:5000';

  constructor(private http: HttpClient) { }

  getFromBackend() {
    const url = `${this.baseUrl}/ruta_a_tu_archivo_python`;
    return this.http.get(url);
  }
}
