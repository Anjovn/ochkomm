import os
pdefolder= os.path.join(os.getcwd(),"pde")
with open("index.html","w") as file: 
    for i in os.listdir(pdefolder):
        folder=os.path.join(pdefolder,i)
        for j in os.listdir(folder):
            file.write(f"<h3>{j}</h3>")
            file.write(f'<canvas class="Processing__canvas" data-processing-sources="pde/{i}/{j}/{j}.pde"></canvas>')
            with open(os.path.join(folder,f"{j}/{j}.pde"),"r") as codefile:
                file.write("<pre><code class='java-html'>")
                for line in codefile.readlines():
                    file.write(f"<p>{line}</p>")
                file.write("</code></pre>")
                
    file.write('<script type="text/javascript" src="processing.js"></script>')




