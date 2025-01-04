import type internal from "stream";

export interface User {
    id: number;
    username: string;
    email: string;
}

export interface Song {
    id: number;
    title: string;
    author: string;
    uploader: number;
    uploader_name: string;
    source: string;
}

export interface Album {
    id: number;
    title: string;
    author: User | null;
    songs: Song[];
}

export interface Cassette {
    id: number;
    title: string;
    author: User | null;
    description?: string;
    color1: string;
    color2: string;
    color3: string;
    accent_color: string;
}
