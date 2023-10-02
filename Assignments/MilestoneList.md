Our project is a research project, so seeing how far we can go is the real goal. However, I believe (and I assume Prateek does as well) that this a poor way of planning. We are planning assuming we will sucessfully complete this project (or at least the map generator), however this is unrealistic.

Our main objectives can be broken down into 3 main parts:
- A map generator
- A character generator
- An item generator

Currently, we are only enumerating for the map generator, as we believe our methods will change as we continue to the other problems, using similar ideas and tooling to our solution to the map generator.

Map Generator Milestones:
- Generation of map objects is consistant
- Generation of maps is consistant
- Maps can be accessed later and iterated upon
- User maps can be iterated upon
- Generation of maps is non graph based

Generation of map objects is consistant
- This means that the images we put in the map are consistant, both in style, coloring, and product. We intend to use some form of computer vision to refuse and accept items. Consistency will be achieved when the 10 most common DnD objects from Inkarnate.com are generated and identified by an off the shelf computer vision system. 95% >= rate for 100 items must be achieved for consistency.

Generation of maps is consistant
- The qualifications for maps are relative location, and lack of anomaly. An example of an anomaly would be an open cave being next to the ocean, which is below sea level but not flooded. We will have a secondary LLM check the first LLM's output using self evaluation. Consistency will be achieved once both positioning (text output by LLM matches graphical output of map, ie rock north of river should have a rock above a river in X,Y) and non-anomaly output reach a combined rating of 95% for 100 outputs.
Maps can be accessed later and iterated upon
- This will be achieved once a map can change features, with commands such as "remove all barrels and replace them with boxes". Once again, 95% 100 tries for consistancy.
User maps can be iterated upon
- This will be achieved once a map can change features added by a human, with commands such as "remove all barrels and replace them with boxes". Once again, 95% 100 tries for consistancy. The distiction is due to the user not automatically adding tags and descriptions to the map, which means we must add a system to allow the LLM to detect and add them.
Generation of maps is non graph based
- This is changing from the current X by Y system of one item per square, to instead allow items to position themselves in coordinates of a larger scale. Consistency will be when 95% of 100 tries do not have overlap of item.


