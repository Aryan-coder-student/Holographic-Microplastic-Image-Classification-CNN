class Frontend:
    def __init__(self):
        pass
    def about_css_front(self):
        css_style = """
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #282c34; /* Dark background */
                    color: #ffffff; /* White text color */
                    line-height: 1.6;
                }
                .container {
                    max-width: 800px;
                    margin: auto;
                    padding: 20px;
                    background-color: #1e1e1e; /* Darker container background */
                    border-radius: 10px;
                    box-shadow: 0 2px 8px rgba(255, 255, 255, 0.1);
                }
                h1, h2, h3, h4 {
                    color: #61dafb; /* Light blue heading color */
                    font-weight: bold;
                }
                h1 {
                    text-align: center;
                    font-size: 36px;
                    margin-bottom: 20px;
                }
                h2 {
                    font-size: 28px;
                    margin-bottom: 10px;
                }
                h3 {
                    font-size: 24px;
                    margin-bottom: 10px;
                }
                h4 {
                    font-size: 20px;
                    margin-bottom: 5px;
                    text-decoration: underline; /* Underline subheadings */
                }
                p, ul, li {
                    font-size: 18px; /* Decreased font size for paragraphs and list items */
                    margin-bottom: 10px;
                    list-style-type: none;
                }
                hr {
                    border: none;
                    height: 2px;
                    background-color: #61dafb; /* Light blue color for horizontal rule */
                    margin: 20px 0;
                }
                .dataset-section {
                    padding: 20px;
                    border: 2px solid #61dafb; /* Border around dataset section */
                    border-radius: 10px;
                    margin-bottom: 20px;
                }
            </style>
            """
        return css_style
    
    def about_html_front(self):
        html_content = """
            <h1>Microplastics &#9842;</h1>

            <p>Microplastics are tiny pieces of plastic debris, typically smaller than 5 millimeters in size. 
            They come from a variety of sources, including the breakdown of larger plastic items like bottles and bags, 
            the abrasion of synthetic clothing like polyester, and the fragmentation of plastic waste in the environment 
            due to factors like sunlight, waves, and physical wear and tear.</p>

            <hr>

            <h2>Effects of Microplastics</h2>
            <ul>
                <li style="font-size: 20px;"> Ingestion:
                    <ul>
                        <li style="font-size: 18px;">&rarr; Marine animals, including fish, seabirds, turtles, and marine mammals, often mistake microplastics for food. When ingested, these particles can accumulate in their digestive systems, leading to blockages, reduced feeding capacity, internal injuries, and malnutrition. In extreme cases, ingestion of microplastics can result in starvation and death.</li>
                    </ul>
                </li>
                <li style="font-size: 20px;">Toxicity:
                    <ul>
                        <li style="font-size: 18px;">&rarr; Microplastics have the ability to adsorb and accumulate toxic chemicals from the surrounding environment, such as pesticides, heavy metals, and persistent organic pollutants. When marine animals ingest microplastics containing these contaminants, they can suffer from toxic effects, including reproductive issues, developmental abnormalities, and organ damage.</li>
                    </ul>
                </li>
                <li style="font-size: 20px;">Disruption of Feeding Behavior:
                    <ul>
                        <li style="font-size: 18px;">&rarr; Microplastics can interfere with the feeding behavior of marine animals. For filter feeders like mussels and certain species of plankton, microplastics can clog their filtering mechanisms, reducing their ability to obtain food and potentially leading to starvation.</li>
                    </ul>
                </li>
                <li style="font-size: 20px;">Transport of Invasive Species:
                    <ul>
                        <li style="font-size: 18px;">&rarr; Microplastics can act as vehicles for the transport of invasive species. Organisms like algae and small invertebrates can attach themselves to microplastic surfaces and hitch a ride across oceans, potentially disrupting ecosystems in new locations.</li>
                    </ul>
                </li>
                <li style="font-size: 20px;">Physical Harm:
                    <ul>
                        <li style="font-size: 18px;">&rarr; Larger pieces of microplastics, such as fragments of plastic bags or fishing nets, can entangle marine animals, causing injuries, impaired movement, and even death. This entanglement can also lead to suffocation or drowning, particularly for marine mammals and sea turtles.</li>
                    </ul>
                </li>
            </ul>
            <hr>

            <h2>Microplastics are used in:</h2>
            <ul>
                <li style="font-size: 20px;"> Cosmetics and Personal Care Products: 
                    <ul>
                        <li style="font-size: 18px;">&rarr; Microplastics, such as microbeads, have been commonly used in exfoliating scrubs, toothpaste, and other personal care products for their abrasive properties. However, many countries have banned the use of microbeads in such products due to their negative environmental impact.</li>
                    </ul>
                </li>
                <li style="font-size: 20px;"> Textiles: 
                    <ul>
                        <li style="font-size: 18px;">&rarr; Synthetic fibers like polyester and nylon, which are made from plastic polymers, are widely used in the textile industry. Through wear and tear, these textiles shed microfibers, which contribute to the microplastic pollution in the environment.</li>
                    </ul>
                </li>
                <li style="font-size: 20px;"> Industrial Abrasives: 
                    <ul>
                        <li style="font-size: 18px;">&rarr; Microplastics can be used as abrasives in industrial processes, such as sandblasting and polishing.</li>
                    </ul>
                </li>
                <li style="font-size: 20px;"> Additives: 
                    <ul>
                        <li style="font-size: 18px;">&rarr; Microplastics can be added to various materials for specific properties. For example, they can be added to paints and coatings to improve durability and weather resistance.</li>
                    </ul>
                </li>
                <li style="font-size: 20px;"> Research: 
                    <ul>
                        <li style="font-size: 18px;">&rarr; Microplastics are also used in scientific research to study their behavior, environmental impact, and potential solutions to mitigate pollution.</li>
                    </ul>
                </li>
                <li style="font-size: 20px;"> Medical Applications: 
                    <ul>
                        <li style="font-size: 18px;">&rarr; Microplastics are sometimes used in medical devices and implants due to their biocompatibility and durability. However, efforts are being made to develop biodegradable alternatives.</li>
                    </ul>
                </li>
                <li style="font-size: 20px;"> Agriculture: 
                    <ul>
                        <li style="font-size: 18px;">&rarr; Microplastics from degraded plastic mulches and synthetic fertilizers can find their way into agricultural soils.</li>
                    </ul>
                </li>
            </ul>
            <br>
            <div class='dataset-section'>
                <h2>About the Microplastic Dataset</h2>
                <p>This dataset contains microplastic particle images used for research purposes, including 'Holographic Classifier: 
                    Deep Learning in Digital Holography for Automatic Micro-objects Classification' and 'Microplastic pollution 
                    monitoring with holographic classification and deep learning.' The dataset is labeled by microplastic type and 
                    number of particles in the image.
                    <a href = "https://github.com/ymzhu19eee/dataset_microplastics"> Dataset Source </p>
            </div>
            """
        return html_content
    def plastic_css_front(self):
        css_style = """
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #282c34; /* Dark background */
                color: #ffffff; /* White text color */
                line-height: 1.6;
            }
            .container {
                max-width: 800px;
                margin: auto;
                padding: 20px;
                background-color: #1e1e1e; /* Darker container background */
                border-radius: 10px;
                box-shadow: 0 2px 8px rgba(255, 255, 255, 0.1);
            }
            h1, h2, h3, h4 {
                color: #61dafb; /* Light blue heading color */
                font-weight: bold;
            }
            h1 {
                text-align: center;
                font-size: 36px;
                margin-bottom: 20px;
            }
            h2 {
                font-size: 28px;
                margin-bottom: 10px;
            }
            h3 {
                font-size: 24px;
                margin-bottom: 10px;
            }
            h4 {
                font-size: 20px;
                margin-bottom: 5px;
                text-decoration: underline; /* Underline subheadings */
            }
            p, ol, li {
                font-size: 18px; /* Decreased font size for paragraphs and list items */
                margin-bottom: 10px;
            }
            ol.square {
                list-style-type: square;
            }
            hr {
                border: none;
                height: 2px;
                background-color: #61dafb; /* Light blue color for horizontal rule */
                margin: 20px 0;
            }
            .dataset-section {
                padding: 20px;
                border: 2px solid #61dafb; /* Border around dataset section */
                border-radius: 10px;
                margin-bottom: 20px;
            }
        </style>
        """
        return css_style
    def plastic_html_front(self):
        html_content = """
            <h1>Microplastics Identification & Descriptions</h1>

            <h2>Microplastic Identification:</h2>
            <ul>
                <li style="font-size: 20px;">Polyethylene (PE):
                    <ul>
                        <li>Commonly found in bags and films.</li>
                    </ul>
                </li>
                <li style="font-size: 20px;">Polystyrene (PS):
                    <ul>
                        <li>Used in packaging and disposable items.</li>
                    </ul>
                </li>
                <li style="font-size: 20px;">Polyhydroxyalkanoate (PHA):
                    <ul>
                        <li>A biodegradable alternative gaining traction.</li>
                    </ul>
                </li>
                <li style="font-size: 20px;">Low-Density Polyethylene (LDPE):
                    <ul>
                        <li>Known for its flexibility and used in food packaging.</li>
                    </ul>
                </li>
                <li style="font-size: 20px;">Mixed Plastic:
                    <ul>
                        <li>A combination of various plastic types.</li>
                    </ul>
                </li>
                <li style="font-size: 20px;">Plastic with dust:
                    <ul>
                        <li>Indicates potential contamination.</li>
                    </ul>
                </li>
            </ul>
            <hr>
            """
        return html_content