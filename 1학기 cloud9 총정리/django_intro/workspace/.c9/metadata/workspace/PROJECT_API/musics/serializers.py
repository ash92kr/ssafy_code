{"filter":false,"title":"serializers.py","tooltip":"/PROJECT_API/musics/serializers.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":28,"column":0},"end":{"row":28,"column":58},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":5,"state":"start","mode":"ace/mode/python"}},"hash":"8b6f166f3ecf83094cbd08892ac9e3290b3aef2c","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":9,"column":54},"end":{"row":9,"column":55},"action":"insert","lines":["m"],"id":189},{"start":{"row":9,"column":55},"end":{"row":9,"column":56},"action":"insert","lines":["a"]},{"start":{"row":9,"column":56},"end":{"row":9,"column":57},"action":"insert","lines":["n"]},{"start":{"row":9,"column":57},"end":{"row":9,"column":58},"action":"insert","lines":["y"]}],[{"start":{"row":9,"column":58},"end":{"row":9,"column":59},"action":"insert","lines":["를"],"id":192}],[{"start":{"row":9,"column":59},"end":{"row":9,"column":60},"action":"insert","lines":[" "],"id":193}],[{"start":{"row":9,"column":60},"end":{"row":9,"column":61},"action":"insert","lines":["써"],"id":197}],[{"start":{"row":9,"column":61},"end":{"row":9,"column":62},"action":"insert","lines":["야"],"id":198}],[{"start":{"row":9,"column":62},"end":{"row":9,"column":63},"action":"insert","lines":[" "],"id":199}],[{"start":{"row":9,"column":63},"end":{"row":9,"column":64},"action":"insert","lines":["한"],"id":202}],[{"start":{"row":9,"column":64},"end":{"row":9,"column":65},"action":"insert","lines":["다"],"id":204}],[{"start":{"row":12,"column":45},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":205},{"start":{"row":13,"column":0},"end":{"row":13,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":8},"action":"remove","lines":["    "],"id":206},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":207}],[{"start":{"row":14,"column":0},"end":{"row":18,"column":45},"action":"insert","lines":["class ArtistSerializer(serializers.ModelSerializer):","    music_set = MusicSerializer(many=True)   # 쿼리셋이므로 many를 써야 한다","    class Meta:","        model = Artist","        fields = ['id', 'name', 'music_set',]"],"id":208}],[{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["D"],"id":210},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["e"]},{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"remove","lines":["t"],"id":211}],[{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":["t"],"id":212},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"insert","lines":["a"]},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"insert","lines":["i"]},{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"insert","lines":["l"]}],[{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"remove","lines":["    music_set = MusicSerializer(many=True)   # 쿼리셋이므로 many를 써야 한다",""],"id":213}],[{"start":{"row":11,"column":31},"end":{"row":11,"column":44},"action":"remove","lines":[" 'music_set',"],"id":214}],[{"start":{"row":17,"column":45},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":215},{"start":{"row":18,"column":0},"end":{"row":18,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":18,"column":4},"end":{"row":18,"column":8},"action":"remove","lines":["    "],"id":216}],[{"start":{"row":18,"column":4},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":217},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"remove","lines":["    "],"id":218}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":1},"action":"insert","lines":["c"],"id":219},{"start":{"row":19,"column":1},"end":{"row":19,"column":2},"action":"insert","lines":["l"]},{"start":{"row":19,"column":2},"end":{"row":19,"column":3},"action":"insert","lines":["a"]},{"start":{"row":19,"column":3},"end":{"row":19,"column":4},"action":"insert","lines":["s"]},{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"insert","lines":["s"]}],[{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"insert","lines":[" "],"id":220},{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"insert","lines":["C"]},{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"insert","lines":["o"]},{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"insert","lines":["m"]},{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"insert","lines":["m"]},{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"insert","lines":["e"]},{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"insert","lines":["n"]}],[{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"insert","lines":["t"],"id":221}],[{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"insert","lines":["S"],"id":222},{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"insert","lines":["e"]},{"start":{"row":19,"column":15},"end":{"row":19,"column":16},"action":"insert","lines":["r"]},{"start":{"row":19,"column":16},"end":{"row":19,"column":17},"action":"insert","lines":["i"]},{"start":{"row":19,"column":17},"end":{"row":19,"column":18},"action":"insert","lines":["a"]},{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"insert","lines":["l"]},{"start":{"row":19,"column":19},"end":{"row":19,"column":20},"action":"insert","lines":["i"]},{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"insert","lines":["z"]},{"start":{"row":19,"column":21},"end":{"row":19,"column":22},"action":"insert","lines":["e"]},{"start":{"row":19,"column":22},"end":{"row":19,"column":23},"action":"insert","lines":["r"]}],[{"start":{"row":19,"column":23},"end":{"row":19,"column":25},"action":"insert","lines":["()"],"id":223}],[{"start":{"row":19,"column":24},"end":{"row":19,"column":25},"action":"insert","lines":["m"],"id":224},{"start":{"row":19,"column":25},"end":{"row":19,"column":26},"action":"insert","lines":["o"]}],[{"start":{"row":19,"column":25},"end":{"row":19,"column":26},"action":"remove","lines":["o"],"id":225},{"start":{"row":19,"column":24},"end":{"row":19,"column":25},"action":"remove","lines":["m"]}],[{"start":{"row":19,"column":24},"end":{"row":19,"column":25},"action":"insert","lines":["s"],"id":226}],[{"start":{"row":19,"column":24},"end":{"row":19,"column":25},"action":"remove","lines":["s"],"id":227},{"start":{"row":19,"column":24},"end":{"row":19,"column":35},"action":"insert","lines":["serializers"]}],[{"start":{"row":19,"column":35},"end":{"row":19,"column":36},"action":"insert","lines":["."],"id":228},{"start":{"row":19,"column":36},"end":{"row":19,"column":37},"action":"insert","lines":["M"]},{"start":{"row":19,"column":37},"end":{"row":19,"column":38},"action":"insert","lines":["o"]}],[{"start":{"row":19,"column":36},"end":{"row":19,"column":38},"action":"remove","lines":["Mo"],"id":229},{"start":{"row":19,"column":36},"end":{"row":19,"column":51},"action":"insert","lines":["ModelSerializer"]}],[{"start":{"row":19,"column":52},"end":{"row":19,"column":53},"action":"insert","lines":[":"],"id":230}],[{"start":{"row":19,"column":53},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":231},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]},{"start":{"row":20,"column":4},"end":{"row":20,"column":5},"action":"insert","lines":["c"]},{"start":{"row":20,"column":5},"end":{"row":20,"column":6},"action":"insert","lines":["l"]},{"start":{"row":20,"column":6},"end":{"row":20,"column":7},"action":"insert","lines":["a"]},{"start":{"row":20,"column":7},"end":{"row":20,"column":8},"action":"insert","lines":["s"]},{"start":{"row":20,"column":8},"end":{"row":20,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":20,"column":9},"end":{"row":20,"column":10},"action":"insert","lines":[" "],"id":232},{"start":{"row":20,"column":10},"end":{"row":20,"column":11},"action":"insert","lines":["M"]},{"start":{"row":20,"column":11},"end":{"row":20,"column":12},"action":"insert","lines":["e"]},{"start":{"row":20,"column":12},"end":{"row":20,"column":13},"action":"insert","lines":["t"]},{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"insert","lines":["a"]},{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"insert","lines":[":"]}],[{"start":{"row":20,"column":15},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":233},{"start":{"row":21,"column":0},"end":{"row":21,"column":8},"action":"insert","lines":["        "]},{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"insert","lines":["m"]},{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"insert","lines":["o"]},{"start":{"row":21,"column":10},"end":{"row":21,"column":11},"action":"insert","lines":["d"]},{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"insert","lines":["e"]},{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"insert","lines":["l"]}],[{"start":{"row":21,"column":13},"end":{"row":21,"column":14},"action":"insert","lines":[" "],"id":234},{"start":{"row":21,"column":14},"end":{"row":21,"column":15},"action":"insert","lines":["="]}],[{"start":{"row":21,"column":15},"end":{"row":21,"column":16},"action":"insert","lines":[" "],"id":235},{"start":{"row":21,"column":16},"end":{"row":21,"column":17},"action":"insert","lines":["C"]},{"start":{"row":21,"column":17},"end":{"row":21,"column":18},"action":"insert","lines":["o"]},{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"insert","lines":["m"]},{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"insert","lines":["m"]},{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"insert","lines":["e"]},{"start":{"row":21,"column":21},"end":{"row":21,"column":22},"action":"insert","lines":["n"]},{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"insert","lines":["t"]}],[{"start":{"row":21,"column":16},"end":{"row":21,"column":23},"action":"remove","lines":["Comment"],"id":236},{"start":{"row":21,"column":16},"end":{"row":21,"column":23},"action":"insert","lines":["Comment"]}],[{"start":{"row":21,"column":16},"end":{"row":21,"column":23},"action":"remove","lines":["Comment"],"id":237},{"start":{"row":21,"column":16},"end":{"row":21,"column":23},"action":"insert","lines":["Comment"]}],[{"start":{"row":21,"column":23},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":238},{"start":{"row":22,"column":0},"end":{"row":22,"column":8},"action":"insert","lines":["        "]},{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"insert","lines":["f"]},{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"insert","lines":["i"]},{"start":{"row":22,"column":10},"end":{"row":22,"column":11},"action":"insert","lines":["e"]},{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"insert","lines":["l"]},{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"insert","lines":["d"]},{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"insert","lines":["s"]}],[{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"insert","lines":[" "],"id":239},{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":["="]}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":[" "],"id":240}],[{"start":{"row":22,"column":17},"end":{"row":22,"column":19},"action":"insert","lines":["[]"],"id":241}],[{"start":{"row":22,"column":18},"end":{"row":22,"column":20},"action":"insert","lines":["''"],"id":242}],[{"start":{"row":22,"column":19},"end":{"row":22,"column":20},"action":"insert","lines":["i"],"id":243},{"start":{"row":22,"column":20},"end":{"row":22,"column":21},"action":"insert","lines":["d"]}],[{"start":{"row":22,"column":22},"end":{"row":22,"column":23},"action":"insert","lines":[","],"id":244}],[{"start":{"row":22,"column":23},"end":{"row":22,"column":24},"action":"insert","lines":[" "],"id":245}],[{"start":{"row":22,"column":24},"end":{"row":22,"column":26},"action":"insert","lines":["''"],"id":246}],[{"start":{"row":22,"column":25},"end":{"row":22,"column":26},"action":"insert","lines":["c"],"id":247},{"start":{"row":22,"column":26},"end":{"row":22,"column":27},"action":"insert","lines":["o"]},{"start":{"row":22,"column":27},"end":{"row":22,"column":28},"action":"insert","lines":["n"]},{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"insert","lines":["t"]},{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"insert","lines":["e"]},{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"insert","lines":["n"]},{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":22,"column":33},"end":{"row":22,"column":34},"action":"insert","lines":[","],"id":248}],[{"start":{"row":22,"column":35},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":249},{"start":{"row":23,"column":0},"end":{"row":23,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":23,"column":4},"end":{"row":23,"column":8},"action":"remove","lines":["    "],"id":250},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":23,"column":0},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":251},{"start":{"row":24,"column":0},"end":{"row":24,"column":1},"action":"insert","lines":["c"]},{"start":{"row":24,"column":1},"end":{"row":24,"column":2},"action":"insert","lines":["l"]},{"start":{"row":24,"column":2},"end":{"row":24,"column":3},"action":"insert","lines":["a"]},{"start":{"row":24,"column":3},"end":{"row":24,"column":4},"action":"insert","lines":["s"]},{"start":{"row":24,"column":4},"end":{"row":24,"column":5},"action":"insert","lines":["s"]}],[{"start":{"row":24,"column":5},"end":{"row":24,"column":6},"action":"insert","lines":[" "],"id":252},{"start":{"row":24,"column":6},"end":{"row":24,"column":7},"action":"insert","lines":["M"]},{"start":{"row":24,"column":7},"end":{"row":24,"column":8},"action":"insert","lines":["u"]}],[{"start":{"row":24,"column":8},"end":{"row":24,"column":9},"action":"insert","lines":["s"],"id":253},{"start":{"row":24,"column":9},"end":{"row":24,"column":10},"action":"insert","lines":["i"]},{"start":{"row":24,"column":10},"end":{"row":24,"column":11},"action":"insert","lines":["c"]},{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"insert","lines":["D"]},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["e"]},{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"insert","lines":["t"]},{"start":{"row":24,"column":14},"end":{"row":24,"column":15},"action":"insert","lines":["i"]},{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"insert","lines":["a"]}],[{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"insert","lines":["l"],"id":254},{"start":{"row":24,"column":17},"end":{"row":24,"column":18},"action":"insert","lines":["S"]}],[{"start":{"row":24,"column":18},"end":{"row":24,"column":19},"action":"insert","lines":["e"],"id":255},{"start":{"row":24,"column":19},"end":{"row":24,"column":20},"action":"insert","lines":["r"]},{"start":{"row":24,"column":20},"end":{"row":24,"column":21},"action":"insert","lines":["i"]},{"start":{"row":24,"column":21},"end":{"row":24,"column":22},"action":"insert","lines":["a"]},{"start":{"row":24,"column":22},"end":{"row":24,"column":23},"action":"insert","lines":["l"]},{"start":{"row":24,"column":23},"end":{"row":24,"column":24},"action":"insert","lines":["i"]},{"start":{"row":24,"column":24},"end":{"row":24,"column":25},"action":"insert","lines":["z"]},{"start":{"row":24,"column":25},"end":{"row":24,"column":26},"action":"insert","lines":["e"]},{"start":{"row":24,"column":26},"end":{"row":24,"column":27},"action":"insert","lines":["r"]}],[{"start":{"row":24,"column":27},"end":{"row":24,"column":29},"action":"insert","lines":["()"],"id":256}],[{"start":{"row":24,"column":28},"end":{"row":24,"column":29},"action":"insert","lines":["s"],"id":257},{"start":{"row":24,"column":29},"end":{"row":24,"column":30},"action":"insert","lines":["e"]}],[{"start":{"row":24,"column":28},"end":{"row":24,"column":30},"action":"remove","lines":["se"],"id":258},{"start":{"row":24,"column":28},"end":{"row":24,"column":39},"action":"insert","lines":["serializers"]}],[{"start":{"row":24,"column":39},"end":{"row":24,"column":40},"action":"insert","lines":["."],"id":259},{"start":{"row":24,"column":40},"end":{"row":24,"column":41},"action":"insert","lines":["M"]},{"start":{"row":24,"column":41},"end":{"row":24,"column":42},"action":"insert","lines":["o"]}],[{"start":{"row":24,"column":40},"end":{"row":24,"column":42},"action":"remove","lines":["Mo"],"id":260},{"start":{"row":24,"column":40},"end":{"row":24,"column":55},"action":"insert","lines":["ModelSerializer"]}],[{"start":{"row":24,"column":56},"end":{"row":24,"column":57},"action":"insert","lines":[":"],"id":261}],[{"start":{"row":24,"column":57},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":262},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]},{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"insert","lines":["c"]},{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"insert","lines":["l"]},{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"insert","lines":["a"]}],[{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"remove","lines":["a"],"id":263},{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"remove","lines":["l"]},{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"remove","lines":["c"]}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"insert","lines":["c"],"id":264},{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"insert","lines":["o"]},{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"insert","lines":["m"]},{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"insert","lines":["m"]},{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"insert","lines":["e"]},{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"insert","lines":["n"]},{"start":{"row":25,"column":10},"end":{"row":25,"column":11},"action":"insert","lines":["t"]},{"start":{"row":25,"column":11},"end":{"row":25,"column":12},"action":"insert","lines":["_"]},{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"insert","lines":["s"]},{"start":{"row":25,"column":13},"end":{"row":25,"column":14},"action":"insert","lines":["e"]},{"start":{"row":25,"column":14},"end":{"row":25,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"insert","lines":[" "],"id":265},{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"insert","lines":["="]}],[{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"insert","lines":[" "],"id":266}],[{"start":{"row":25,"column":18},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":267},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "]},{"start":{"row":26,"column":4},"end":{"row":26,"column":5},"action":"insert","lines":["\\"]}],[{"start":{"row":26,"column":4},"end":{"row":26,"column":5},"action":"remove","lines":["\\"],"id":268}],[{"start":{"row":26,"column":4},"end":{"row":26,"column":5},"action":"insert","lines":["c"],"id":269},{"start":{"row":26,"column":5},"end":{"row":26,"column":6},"action":"insert","lines":["l"]},{"start":{"row":26,"column":6},"end":{"row":26,"column":7},"action":"insert","lines":["a"]},{"start":{"row":26,"column":7},"end":{"row":26,"column":8},"action":"insert","lines":["s"]},{"start":{"row":26,"column":8},"end":{"row":26,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":26,"column":9},"end":{"row":26,"column":10},"action":"insert","lines":[" "],"id":270},{"start":{"row":26,"column":10},"end":{"row":26,"column":11},"action":"insert","lines":["M"]},{"start":{"row":26,"column":11},"end":{"row":26,"column":12},"action":"insert","lines":["e"]},{"start":{"row":26,"column":12},"end":{"row":26,"column":13},"action":"insert","lines":["t"]},{"start":{"row":26,"column":13},"end":{"row":26,"column":14},"action":"insert","lines":["a"]},{"start":{"row":26,"column":14},"end":{"row":26,"column":15},"action":"insert","lines":[":"]}],[{"start":{"row":26,"column":15},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":271},{"start":{"row":27,"column":0},"end":{"row":27,"column":8},"action":"insert","lines":["        "]},{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["m"]},{"start":{"row":27,"column":9},"end":{"row":27,"column":10},"action":"insert","lines":["o"]},{"start":{"row":27,"column":10},"end":{"row":27,"column":11},"action":"insert","lines":["d"]},{"start":{"row":27,"column":11},"end":{"row":27,"column":12},"action":"insert","lines":["e"]},{"start":{"row":27,"column":12},"end":{"row":27,"column":13},"action":"insert","lines":["l"]}],[{"start":{"row":27,"column":13},"end":{"row":27,"column":14},"action":"insert","lines":[" "],"id":272},{"start":{"row":27,"column":14},"end":{"row":27,"column":15},"action":"insert","lines":["="]}],[{"start":{"row":27,"column":15},"end":{"row":27,"column":16},"action":"insert","lines":[" "],"id":273},{"start":{"row":27,"column":16},"end":{"row":27,"column":17},"action":"insert","lines":["M"]},{"start":{"row":27,"column":17},"end":{"row":27,"column":18},"action":"insert","lines":["u"]},{"start":{"row":27,"column":18},"end":{"row":27,"column":19},"action":"insert","lines":["s"]},{"start":{"row":27,"column":19},"end":{"row":27,"column":20},"action":"insert","lines":["i"]},{"start":{"row":27,"column":20},"end":{"row":27,"column":21},"action":"insert","lines":["c"]}],[{"start":{"row":27,"column":16},"end":{"row":27,"column":21},"action":"remove","lines":["Music"],"id":274},{"start":{"row":27,"column":16},"end":{"row":27,"column":21},"action":"insert","lines":["Music"]}],[{"start":{"row":27,"column":21},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":275},{"start":{"row":28,"column":0},"end":{"row":28,"column":8},"action":"insert","lines":["        "]},{"start":{"row":28,"column":8},"end":{"row":28,"column":9},"action":"insert","lines":["f"]},{"start":{"row":28,"column":9},"end":{"row":28,"column":10},"action":"insert","lines":["i"]},{"start":{"row":28,"column":10},"end":{"row":28,"column":11},"action":"insert","lines":["e"]},{"start":{"row":28,"column":11},"end":{"row":28,"column":12},"action":"insert","lines":["l"]},{"start":{"row":28,"column":12},"end":{"row":28,"column":13},"action":"insert","lines":["d"]},{"start":{"row":28,"column":13},"end":{"row":28,"column":14},"action":"insert","lines":["s"]}],[{"start":{"row":28,"column":14},"end":{"row":28,"column":15},"action":"insert","lines":[" "],"id":276},{"start":{"row":28,"column":15},"end":{"row":28,"column":16},"action":"insert","lines":["="]}],[{"start":{"row":28,"column":16},"end":{"row":28,"column":17},"action":"insert","lines":[" "],"id":277}],[{"start":{"row":28,"column":17},"end":{"row":28,"column":19},"action":"insert","lines":["[]"],"id":278}],[{"start":{"row":28,"column":18},"end":{"row":28,"column":20},"action":"insert","lines":["''"],"id":279}],[{"start":{"row":28,"column":19},"end":{"row":28,"column":20},"action":"insert","lines":["i"],"id":280},{"start":{"row":28,"column":20},"end":{"row":28,"column":21},"action":"insert","lines":["d"]}],[{"start":{"row":28,"column":22},"end":{"row":28,"column":23},"action":"insert","lines":[","],"id":281}],[{"start":{"row":28,"column":23},"end":{"row":28,"column":24},"action":"insert","lines":[" "],"id":282}],[{"start":{"row":28,"column":24},"end":{"row":28,"column":26},"action":"insert","lines":["''"],"id":283}],[{"start":{"row":28,"column":25},"end":{"row":28,"column":26},"action":"insert","lines":["c"],"id":284},{"start":{"row":28,"column":26},"end":{"row":28,"column":27},"action":"insert","lines":["o"]},{"start":{"row":28,"column":27},"end":{"row":28,"column":28},"action":"insert","lines":["n"]},{"start":{"row":28,"column":28},"end":{"row":28,"column":29},"action":"insert","lines":["t"]},{"start":{"row":28,"column":29},"end":{"row":28,"column":30},"action":"insert","lines":["e"]},{"start":{"row":28,"column":30},"end":{"row":28,"column":31},"action":"insert","lines":["n"]},{"start":{"row":28,"column":31},"end":{"row":28,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":28,"column":33},"end":{"row":28,"column":34},"action":"insert","lines":[","],"id":285}],[{"start":{"row":28,"column":34},"end":{"row":28,"column":35},"action":"insert","lines":[" "],"id":286}],[{"start":{"row":28,"column":35},"end":{"row":28,"column":37},"action":"insert","lines":["''"],"id":287}],[{"start":{"row":28,"column":36},"end":{"row":28,"column":37},"action":"insert","lines":["c"],"id":288},{"start":{"row":28,"column":37},"end":{"row":28,"column":38},"action":"insert","lines":["o"]},{"start":{"row":28,"column":38},"end":{"row":28,"column":39},"action":"insert","lines":["m"]},{"start":{"row":28,"column":39},"end":{"row":28,"column":40},"action":"insert","lines":["m"]},{"start":{"row":28,"column":40},"end":{"row":28,"column":41},"action":"insert","lines":["e"]},{"start":{"row":28,"column":41},"end":{"row":28,"column":42},"action":"insert","lines":["n"]},{"start":{"row":28,"column":42},"end":{"row":28,"column":43},"action":"insert","lines":["t"]},{"start":{"row":28,"column":43},"end":{"row":28,"column":44},"action":"insert","lines":["_"]}],[{"start":{"row":28,"column":44},"end":{"row":28,"column":45},"action":"insert","lines":["s"],"id":289},{"start":{"row":28,"column":45},"end":{"row":28,"column":46},"action":"insert","lines":["e"]},{"start":{"row":28,"column":46},"end":{"row":28,"column":47},"action":"insert","lines":["t"]}],[{"start":{"row":28,"column":48},"end":{"row":28,"column":49},"action":"insert","lines":[","],"id":290}],[{"start":{"row":25,"column":18},"end":{"row":25,"column":19},"action":"insert","lines":["C"],"id":291},{"start":{"row":25,"column":19},"end":{"row":25,"column":20},"action":"insert","lines":["o"]},{"start":{"row":25,"column":20},"end":{"row":25,"column":21},"action":"insert","lines":["m"]},{"start":{"row":25,"column":21},"end":{"row":25,"column":22},"action":"insert","lines":["m"]},{"start":{"row":25,"column":22},"end":{"row":25,"column":23},"action":"insert","lines":["e"]},{"start":{"row":25,"column":23},"end":{"row":25,"column":24},"action":"insert","lines":["n"]},{"start":{"row":25,"column":24},"end":{"row":25,"column":25},"action":"insert","lines":["t"]}],[{"start":{"row":25,"column":18},"end":{"row":25,"column":25},"action":"remove","lines":["Comment"],"id":292},{"start":{"row":25,"column":18},"end":{"row":25,"column":37},"action":"insert","lines":["CommentSerializer()"]}],[{"start":{"row":25,"column":36},"end":{"row":25,"column":37},"action":"insert","lines":["m"],"id":293},{"start":{"row":25,"column":37},"end":{"row":25,"column":38},"action":"insert","lines":["a"]},{"start":{"row":25,"column":38},"end":{"row":25,"column":39},"action":"insert","lines":["n"]},{"start":{"row":25,"column":39},"end":{"row":25,"column":40},"action":"insert","lines":["y"]},{"start":{"row":25,"column":40},"end":{"row":25,"column":41},"action":"insert","lines":["="]},{"start":{"row":25,"column":41},"end":{"row":25,"column":42},"action":"insert","lines":["T"]},{"start":{"row":25,"column":42},"end":{"row":25,"column":43},"action":"insert","lines":["r"]},{"start":{"row":25,"column":43},"end":{"row":25,"column":44},"action":"insert","lines":["u"]},{"start":{"row":25,"column":44},"end":{"row":25,"column":45},"action":"insert","lines":["e"]}],[{"start":{"row":28,"column":25},"end":{"row":28,"column":32},"action":"remove","lines":["content"],"id":294},{"start":{"row":28,"column":25},"end":{"row":28,"column":26},"action":"insert","lines":["t"]},{"start":{"row":28,"column":26},"end":{"row":28,"column":27},"action":"insert","lines":["i"]},{"start":{"row":28,"column":27},"end":{"row":28,"column":28},"action":"insert","lines":["t"]},{"start":{"row":28,"column":28},"end":{"row":28,"column":29},"action":"insert","lines":["l"]},{"start":{"row":28,"column":29},"end":{"row":28,"column":30},"action":"insert","lines":["e"]}],[{"start":{"row":28,"column":32},"end":{"row":28,"column":33},"action":"insert","lines":[" "],"id":295}],[{"start":{"row":28,"column":33},"end":{"row":28,"column":35},"action":"insert","lines":["''"],"id":296}],[{"start":{"row":28,"column":34},"end":{"row":28,"column":35},"action":"insert","lines":["a"],"id":297},{"start":{"row":28,"column":35},"end":{"row":28,"column":36},"action":"insert","lines":["r"]},{"start":{"row":28,"column":36},"end":{"row":28,"column":37},"action":"insert","lines":["t"]},{"start":{"row":28,"column":37},"end":{"row":28,"column":38},"action":"insert","lines":["i"]},{"start":{"row":28,"column":38},"end":{"row":28,"column":39},"action":"insert","lines":["s"]},{"start":{"row":28,"column":39},"end":{"row":28,"column":40},"action":"insert","lines":["t"]}],[{"start":{"row":28,"column":41},"end":{"row":28,"column":42},"action":"insert","lines":[","],"id":298}]]},"timestamp":1556001552610}