























players = {
    "J-Vermell":{
        "nom":"V",
        "carrers":[],
        "diners":2000,
        "cartes":[]
    },
    "J-Groc":{
        "nom":"G",
        "carrers":[],
        "diners":2000,
        "cartes":[]
    },
    "J-Taronja":{
        "nom":"T",
        "carrers":[],
        "diners":2000,
        "cartes":[]
    },
    "J-Blau":{
        "nom":"B",
        "carrers":[],
        "diners":2000,
        "cartes":[]
    },
}











# Los precios estan bien

preus = {
    "Lauria": {
        "Ll. Casa": 10,
        "Ll. Hotel": 15,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 200,
        "Cmp. Hotel": 250
    },
    "Rosselló": {
        "Ll. Casa": 10,
        "Ll. Hotel": 15,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 225,
        "Cmp. Hotel": 255
    },
    "Marina": {
        "Ll. Casa": 15,
        "Ll. Hotel": 15,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 250,
        "Cmp. Hotel": 260
    },
    "C. de cent": {
        "Ll. Casa": 15,
        "Ll. Hotel": 20,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 275,
        "Cmp. Hotel": 265
    },
    "Muntaner": {
        "Ll. Casa": 20,
        "Ll. Hotel": 20,
        "Cmp. Trrny": 60,
        "Cmp. Casa": 300,
        "Cmp. Hotel": 270
    },
    "Aribau": {
        "Ll. Casa": 20,
        "Ll. Hotel": 20,
        "Cmp. Trrny": 60,
        "Cmp. Casa": 325,
        "Cmp. Hotel": 275
    },
    "Sant Joan": {
        "Ll. Casa": 25,
        "Ll. Hotel": 25,
        "Cmp. Trrny": 60,
        "Cmp. Casa": 350,
        "Cmp. Hotel": 280
    },
    "Aragó": {
        "Ll. Casa": 25,
        "Ll. Hotel": 25,
        "Cmp. Trrny": 60,
        "Cmp. Casa": 375,
        "Cmp. Hotel": 285
    },
    "Urquinaona": {
        "Ll. Casa": 30,
        "Ll. Hotel": 25,
        "Cmp. Trrny": 70,
        "Cmp. Casa": 400,
        "Cmp. Hotel": 290
    },
    "Fontana": {
        "Ll. Casa": 30,
        "Ll. Hotel": 30,
        "Cmp. Trrny": 70,
        "Cmp. Casa": 425,
        "Cmp. Hotel": 300
    },
    "Les Rambles": {
        "Ll. Casa": 35,
        "Ll. Hotel": 30,
        "Cmp. Trrny": 70,
        "Cmp. Casa": 450,
        "Cmp. Hotel": 310
    },
    "Pl. Catalunya": {
        "Ll. Casa": 35,
        "Ll. Hotel": 30,
        "Cmp. Trrny": 70,
        "Cmp. Casa": 475,
        "Cmp. Hotel": 320
    },
    "P. Àngel": {
        "Ll. Casa": 40,
        "Ll. Hotel": 35,
        "Cmp. Trrny": 80,
        "Cmp. Casa": 500,
        "Cmp. Hotel": 330
    },
    "Via Augusta": {
        "Ll. Casa": 40,
        "Ll. Hotel": 35,
        "Cmp. Trrny": 80,
        "Cmp. Casa": 525,
        "Cmp. Hotel": 340
    },
    "Balmes": {
        "Ll. Casa": 50,
        "Ll. Hotel": 40,
        "Cmp. Trrny": 80,
        "Cmp. Casa": 550,
        "Cmp. Hotel": 350
    },
    "Pg. de Gràcia": {
        "Ll. Casa": 50,
        "Ll. Hotel": 50,
        "Cmp. Trrny": 80,
        "Cmp. Casa": 525,
        "Cmp. Hotel": 360
    }
}







tablero = {
    "Sortida": {"posicion": 0}, 

    "Lauria": {"posicion": 1, "precio": preus["Lauria"]["Cmp. Trrny"], "casas": 0, "hoteles": 0},
    "Rossell": {"posicion": 2, "precio": preus["Rosselló"]["Cmp. Trrny"], "casas": 0, "hoteles": 0},

    "Sort": {"posicion": 3},  

    "Marina": {"posicion": 4, "precio": preus["Marina"]["Cmp. Trrny"], "casas": 0, "hoteles": 0},
    "Consell": {"posicion": 5, "precio": preus["C. de cent"]["Cmp. Trrny"], "casas": 0, "hoteles": 0},

    "Presó": {"posicion": 6},

    "Muntan": {"posicion": 7, "precio": preus["Muntaner"]["Cmp. Trrny"], "casas": 0, "hoteles": 0},
    "Aribau": {"posicion": 8, "precio": preus["Aribau"]["Cmp. Trrny"], "casas": 0, "hoteles": 0},

    "Caixa": {"posicion": 9},  

    "S.Joan": {"posicion": 10, "precio": preus["Sant Joan"]["Cmp. Trrny"], "casas": 0, "hoteles": 0},
    "Aragó": {"posicion": 11, "precio": preus["Aragó"]["Cmp. Trrny"], "casas": 0, "hoteles": 0},

    "Parking": {"posicion": 12},

    "Urquina": {"posicion": 13, "precio": preus["Urquinaona"]["Cmp. Trrny"], "casas": 0, "hoteles": 0},
    "Fontan": {"posicion": 14, "precio": preus["Fontana"]["Cmp. Trrny"], "casas": 0, "hoteles": 0},

    "Sort 2": {"posicion": 15},

    "Rambles": {"posicion": 16, "precio": preus["Les Rambles"]["Cmp. Trrny"], "casas": 0, "hoteles": 0},
    "Pl.Cat": {"posicion": 17, "precio": preus["Pl. Catalunya"]["Cmp. Trrny"], "casas": 0, "hoteles": 0},

    "Anr pró": {"posicion": 18},

    "P.Àngel": {"posicion": 19, "precio": preus["P. Àngel"]["Cmp. Trrny"], "casas": 0, "hoteles": 0},
    "Augusta": {"posicion": 20, "precio": preus["Via Augusta"]["Cmp. Trrny"], "casas": 0, "hoteles": 0},

    "Caixa 2": {"posicion": 21}, 

    "Balmes": {"posicion": 22, "precio": preus["Balmes"]["Cmp. Trrny"], "casas": 0, "hoteles": 0},
    "Gràcia": {"posicion": 23, "precio": preus["Pg. de Gràcia"]["Cmp. Trrny"], "casas": 0, "hoteles": 0},
}
