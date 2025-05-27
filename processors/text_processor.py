import re
import tkinter as tk
import unicodedata

class TextProcessor:
    def __init__(self, gui):
        self.gui = gui
        self.productDescription = ""
        self.paragraphs = []
        self.productName = ""
        self.readyToUse = ""
        self.imageFileName = ""
        self.templateLength = 4
        self.selectedType = 1
        self.filename_source = 'name'
        
        
    def getData(self):
        self.productDescription = self.gui.textWindowTab1.get("1.0", "end-1c")
        self.paragraphs = self.productDescription.split('\n')
        self.paragraphs = list(filter(lambda par: par != "", self.paragraphs)) 
        self.productName = self.paragraphs[0]
        self.templateLength = len(self.paragraphs) // 2 


    def generateImageFileName(self):
        if self.filename_source == 'code' and hasattr(self, 'image_urls'):
            for url in self.image_urls:
                self.readyToUse = self.readyToUse.replace(
                    "https://media.komputronik.pl/pl-komputronik/img/opisy_produktow/content/SEO/IMAGENAME.jpg",
                    url,
                    1
                )
            self.readyToUse = re.sub(
            r'<div class="col-2-5[^>]*>.*?IMAGENAME\.jpg"[^>]*>.*?</div>',
            '',
            self.readyToUse,
            flags=re.DOTALL
            )    
                
            self.gui.imageNameEntryTab1.delete(0, tk.END)
            self.gui.imageNameEntryTab1.insert(0, "<grafiki: galeria karty produktu>")
            return
        
        base = unicodedata.normalize('NFKD', self.productName).encode('ascii', 'ignore').decode()                                          
        base = re.sub(r'[^A-Za-z0-9]+', '-', base)                     
        base = base.strip('-').lower()                                 

        for i in range(1, self.templateLength + 1):
            img_name = f"{base}-{i}"
            self.readyToUse = self.readyToUse.replace("IMAGENAME", img_name, 1)

        self.gui.imageNameEntryTab1.delete(0, tk.END)
        self.gui.imageNameEntryTab1.insert(0, base + "-")


    def fillTemplate(self, productName, paragraphs):
        fragments = []
        
        header = paragraphs[0] if len(paragraphs) > 0 else ""
        text = paragraphs[1] if len(paragraphs) > 1 else ""


        separatorElement = f"""<div class="separator short"></div>"""
        
       
        mainTemplateElementCenter = f"""<div class="col-3-3 m-center">
                                        <p>

                                        {text}

                                        </p>
                                        </div>

                                        <div class="col-3-3 center">

                                        <img src="https://media.komputronik.pl/pl-komputronik/img/opisy_produktow/content/SEO/IMAGENAME.jpg" style="max-width:80%; padding:10%!important; background:#fff" alt=""/>


                                        </div>

                                        <!--img koniec-->





                                        <div class="separator short"></div>


                                        <!-- header-->
                                        <div class="col-3-3">

                                        <h3>
                                                               {header}
                                        </h3>
                                        </div>
                                        <!-- end header-->"""
        
     
        mainTemplateElementLeft = f"""<div class="col-3-3 cc-mobile">
                                    <div class="col-2-5 cc-mobile-2">
                                    <img src="https://media.komputronik.pl/pl-komputronik/img/opisy_produktow/content/SEO/IMAGENAME.jpg" class="left" style="max-width:80%; padding:10%!important; background:#fff" alt=""/>
                                    </div>
                                    <div class="col-3-5 cc-mobile-1">

                                    <p>
                                    
                                    {text}

                                    </p>
                                    </div>
                                    </div>
                                    <div class="separator short"></div>


                                    <!-- header-->
                                    <div class="col-3-3">

                                    <h3>
                                    
                                    {header}

                                    </h3>
                                    </div>
                                    <!-- end header-->"""                

        mainTemplateElementMini = f"""<div class="col-3-3 cc-mobile">
                                    <div class="col-2-5 cc-mobile-2">
                                    <img src="https://media.komputronik.pl/pl-komputronik/img/opisy_produktow/content/SEO/IMAGENAME.jpg" class="left" style="max-width:80%; padding:10%!important; background:#fff" alt=""/>
                                    </div>
                                    <div class="col-3-5 cc-mobile-1">
                                    <h3>
                                    
                                    {header}
                                    </h3>
                                     <p>
                                    
                                    {text}

                                    </p>
                                    </div>
                                    </div>"""

        if self.selectedType == 1:
            fragments.append(mainTemplateElementCenter)
        elif self.selectedType == 2:
            fragments.append(mainTemplateElementLeft)
        else: 
            fragments.append(mainTemplateElementMini)

        for i in range(2, len(paragraphs), 2):
            header = paragraphs[i] if i < len(paragraphs) else ""
            text = paragraphs[i+1] if i+1 < len(paragraphs) else ""

            if self.selectedType == 3:
                templateElementMini = f"""<div class="col-5-6 m-center">
                                        <h3>
                                            {header}
                                        </h3>
                                        <p> 
                                            {text}
                                        </p>
                                        </div> """
                
                fragments.append(templateElementMini.replace("{header}", header).replace("{text}", text))

            else:    
                
                templateElementLeft = f"""<div class="col-3-3 cc-mobile bg-gray-porcelain rounded-2xl">
                                        <div class="col-2-5 cc-mobile-2">
                                        <img src="https://media.komputronik.pl/pl-komputronik/img/opisy_produktow/content/SEO/IMAGENAME.jpg" class="left" style="max-width:80%; padding:10%!important; background:#fff" alt=""/>
                                        </div>
                                        <div class="col-3-5 cc-mobile-1">
                                        <h4>
                                        
                                        {header}
                                        
                                        </h4>
                                        <p>
                                        
                                        {text}
                                        
                                        </p>
                                        </div>
                                        </div>"""
    
                templateElementRight = f"""<div class="col-3-3 cc-mobile bg-gray-porcelain rounded-2xl">
                                        <div class="col-3-5 cc-mobile-1 ">
                                        <h4>
                                        {header}
                                        
                                        </h4>
                                        <p>
                                        
                                        {text}
                                        
                                        </p>
                                        </div>
                                        <div class="col-2-5 cc-mobile-2">
                                        <img src="https://media.komputronik.pl/pl-komputronik/img/opisy_produktow/content/SEO/IMAGENAME.jpg" class="left" style="max-width:80%; padding:10%!important; background:#fff" alt=""/>
                                        </div>
                                        
                                        </div>"""
                if (i // 2) % 2 == 0:
                    fragments.append(templateElementRight.replace("{header}", header).replace("{text}", text))
                else: 
                    fragments.append(templateElementLeft.replace("{header}", header).replace("{text}", text))

                if (i + 2) < len(paragraphs):
                    fragments.append(separatorElement)

        if self.selectedType != 3:
            self.readyToUse = separatorElement.join(fragments)
        else: 
            filler = ""
            self.readyToUse = filler.join(fragments)

     
    def generateSEO(self):
        self.getData()
        self.fillTemplate(self.productName, self.paragraphs)
        self.generateImageFileName()
        
        self.gui.HTMLWindowTab1.delete("1.0", tk.END)  
        self.gui.HTMLWindowTab1.insert("1.0", self.readyToUse)
        
        self.gui.HTMLWindowTab2.delete("1.0", tk.END)  
        self.gui.HTMLWindowTab2.insert("1.0", self.readyToUse)
        
        self.gui.textWindowTab2.delete("1.0", tk.END)

        self.gui.HTMLWindowTab3.delete("1.0", tk.END)  
        self.gui.HTMLWindowTab3.insert("1.0", self.readyToUse)