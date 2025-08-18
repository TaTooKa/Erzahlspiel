Space Physics
=============

.. figure:: /_static/images/rpg-image-16.jpg

   art © `Maciej Rebisz <https://www.artstation.com/artwork/8BW5DE>`_

INTERPLANETARY is a roleplaying game setting that attempts to create an immersive and educational experience.

By integrating accurate scientific principles, players are encouraged to engage with the complexities of space travel, such as gravitational forces, orbital mechanics, and the effects of different propulsion systems. This not only enhances the realism of the game but also fosters a deeper understanding of the universe. Players must think critically about their actions, calculating transit times or considering the implications of gravity, radiation, pressure, and other physical and chemical phenomena, which adds a layer of strategy and intellectual challenge to the gameplay.

Moreover, emphasizing space physics allows for richer storytelling and character development within the game. As players navigate challenges based on real scientific concepts, they can explore themes of exploration, survival, and innovation in a scientifically plausible context. This approach not only captivates players who are fans of science fiction but also attracts those interested in science and technology. By grounding the narrative in hard science, INTERPLANETARY can serve as a platform for education and inspiration, sparking curiosity about space exploration and the scientific principles that govern it.

Which is why this section goes full-on *hard-sci-fi* concepts and space physics.

Gravity
-------

.. figure:: /_static/images/rpg-image-17.jpg

   art © `Xiaopeng Shen <https://www.artstation.com/artwork/ozlZq>`_


In space there is no gravity, unless you make it artificially by centrifugal force or thrust.

Artificial gravity
~~~~~~~~~~~~~~~~~~

There are two methods to generate artificial gravity: **Thrust** and **Centrifugal force**.

Thrust
^^^^^^

**Thrust** is the easiest one (but not the cheapest): It consists of maintaining a constant acceleration in a vessel, thus pushing “down” everything inside it. If the spacecraft is accelerating at 0.5G, everyone aboard would be experiencing a force pushing them down (or against the thrust vector) akin to 0.5 gravity. This is not a reliable source of artificial gravity for two reasons:

- **You can’t accelerate forever**; eventually you need to stop (ideally, when you reach your destination). The most common maneuver, the "Brachistochrone", is to constantly accelerate for half the trip, then rotate and fire your thrusters in the opposite direction, decelerating (or breaking) for the second half of the trip. This would generate constant artificial gravity for the entirety of the journey, but… most vessels do a partial burn and drift (in Zero-G) for a portion of the trip (to save fuel and propellant).
- **Fuel isn’t cheap**, and mass ratio must be taken into account. Some advanced fusion engines (with Deuterium-Helium³ fuel cycles) are extremely efficient and have seen incredible performance breakthroughs, but for most other commonly used engines, this option might be prohibitive (economically or physically).

Centrifugal Force
^^^^^^^^^^^^^^^^^

**Centrifugal Force** is achieved by rotating the vessel or habitat around a central axis. This way, everything inside it would experience a force pushing it towards the outside boundaries (away from the center). This is the most commonly used method of artificial gravity in most space stations and even some vessels. The main drawback is the *Coriolis Effect* (a sideways motion created by the spin). The smaller the vessel (or the closer to the central axis), the more pronounced this effect is, and it can be powerful enough to cause dizziness or nausea (represented as a Condition like ``Coriolis vertigo (Mild, -1)``). This force can also cause unwanted physical side-effects, for example, throwing a ball spinward would make it fall faster, but throwing it anti-spinward would make it float for longer. Pouring water out of a kettle will cause the water to fall slightly anti-spinward, etc.

Zero gravity
~~~~~~~~~~~~

The human anatomy (specially if grown on Earth, Mars, or other gravity wells) is not made for microgravity, or Zero-G. The body slowly deteriorates and it can be fatal after 5 years if no measures are taken. This is represented mechanically by the character gaining an increasing number of stacking Conditions over time, specially after 1 year of exposure [#]_.

.. [#] Due to the amount of Conditions, the character becomes unplayable. Retire it and create a new one.

.. csv-table:: Extended effects of Zero-G on the human body
   :header: "Time in Zero-G","Effect / Condition"
   :widths: 20, 80

   "instant","Fluids pool in the chest and face, making you puffy and uncomfortable. 
   
   Gain ``Zero-G discomfort (Mild, -1)``"
   "1 week","Lower blood pressure and loss of potassium and liquids. 
   
   Gain ``Zero-G dehydration (Mild, -1)``"
   "1 month","Muscle atrophy and reduced body mass. 
   
   Gain ``Zero-G atrophy (Moderate, -3)``"
   "3 months","Bones begin to lose calcium, becoming weak and brittle. 
   
   Gain ``Spaceflight osteopenia (Severe, -5)``"
   "1 year","Bodily functions begin to collapse; You are probably blind, and are quasi-paralysed or prostrate without some sort of assistance."
   "5 years","Your body completely collapses. You will imminently die of cardiac arrest, circulatory system collapse, ischemic stroke or similar causes."


.. admonition:: Low gravity

   If exposed to gravity greater than 0 but lower than half your :hoverxref:`native gravity <nativegravity>`, the effects of Zero-G still apply, but take 4X the time to kick in.

.. figure:: /_static/images/0G-effects.png

These effects can be countered or postponed by doing one or more of the following:

.. csv-table:: 
   :header: "Preventive Action","Outcome"
   :widths: 20, 80

   "**Taking drugs**
   
   (calcium tabs, water retention aids, vasoconstrictors, etc)", "Delay most Zero-G health effects, for a maximum of 1 month (after that, effects start to apply as normal). Excessive use might lead to addiction or dependency."
   "**Physical Exercise**
   
   (treadmill, cycling, weight-pushing, muscle stress, etc)", "Ignore all Zero-G health effects.

   - At first, 1 hour/day is enough.
   - After 1 month, 2 hours/day are required.
   - After 3 months, 4 hours/day are required.
   - After 6 months, even constant exercise won’t be enough, and zero-g effects will start to occur as normal."
   "**Exposure to Gravity**

   (thrust, centrifugal force or a true gravity well)", "At least 1 hour of your native gravity for every 3 days in Zero-G is enough to “pause” Zero-G health deterioration completely.
   
   If under lower Gs, adjust the hours/days relation accordingly (i.e. at least 2hs of [½ native G] per 3 days in Zero-G)." 
   "**Tensile Strength Clothing**

   (G-suits, built-in elastic strap, “penguin suits”, etc)", "By forcing the body into positions which cause the muscles to exert extra force to counteract its resistance, these suits help delay the effects of Zero-G health deterioration by +50% (i.e. it would take one and a half weeks to suffer **dehydration**, one and a half months to suffer **atrophy**, etc)."
   "**Zero-G Experience**

   (Having lived most of your life in Zero-G environments, years of experience working in microgravity, etc)", "Ignore the basic effects of Zero-G **discomfort**. The puffiness still happens; you are just accustomed to it enough that it doesn’t affect you at all."

.. tip::

 The Condition ``Zero-G discomfort (Mild, -1)`` (which is automatically gained by anyone exposed to Zero-G for the first time) also represents the awkwardness of operating in free-fall: The need to accustom oneself to use anchor points, hand-holds, tethers or thrusters; the miscalculations of your body movements and misjudgements in applied strength; the inexperience in constantly being upside down or bumping into everything; etc. Thus, having **Zero-G Experience** cancels this Condition altogether.

High gravity
~~~~~~~~~~~~

Just like low or zero gravity is detrimental to human health in the long term, so is high gravity exposure… It just affects you much, much faster.

There are not many places in the Solar System with High Gravity (or where other factors won’t kill you first). The only realistic way to expose oneself to High-Gs is to be in a vessel that is constantly accelerating (long periods) or doing hard maneuvers (short bursts).

Each character has a :hoverxref:`native gravity <nativegravity>` they are accustomed to (because it’s how they grew, or because of years of experience). Check on the following table to see what are the effects of High-G exposure, depending on your “native gravity”:

.. csv-table:: Effects of High-G on the human body
   :header: "Exposed to High-G","Effect / Condition"
   :widths: 20, 80

   "2x your native gravity", "everything feels like it weighs double as normal (even your body, clothes, tools, etc).
   
   - **Short burst**: although discomforting, negligible for most people.
   - **Long period**: Gain the ``Hindered by High-G (Moderate, -3)`` Condition, and lose 1 HP immediately and 1 HP for every hour of continuous exposure."
   "3x your native gravity", "- **Short burst**: make a :hoverxref:`high-G burst check <highgburstcheck>`.
   - **Long period**: Gain the ``Restrained by High-G (Severe, -5)`` Condition. Lose 2 HP immediately and 2 HP for every hour of continuous exposure."
   "4x your native gravity", "- **Short burst**: Lose 1 HP. Make a :hoverxref:`high-G burst check <highgburstcheck>`.
   - **Long period**: You cannot move (maybe a little bit if you make extreme effort, otherwise you are prostrate in place). Lose 3 HP immediately and 3 HP for every hour of continuous exposure."
   "5x your native gravity", "- **Short burst**: Lose 3 HP. Make a :hoverxref:`high-G burst check <highgburstcheck>`.
   - **Long period**: You cannot move ― you are prostrate in place and in severe pain. Lose 4 HP Immediately and 4 HP for every hour of continuous exposure."
   "10x your native gravity, or more", "- **Short burst**: Lose 5 HP. Make a :hoverxref:`high-G burst check <highgburstcheck>`.
   - **Long period**: You cannot move ― you are prostrate in place and in severe pain. Lose 5 HP Immediately and 5 HP for every hour of continuous exposure."

.. _highgburstcheck:

High-G Burst Check
^^^^^^^^^^^^^^^^^^

Make a dice roll modified by any skill that might help you resist a burst of High-G, with a difficulty set by the amount of Gs resisted in relation to your native gravity [#]_. 

- On a **stalemate** or a **success**, you resist the effects of the High-G burst.
- On a **failure**...:

   - If the :hoverxref:`Negative Effect <effect>` is 5 or less, you lose 1 HP and gain the ``Tunnel Vision (Mild, -1)`` Condition for [Effect] minutes. 
   - If the :hoverxref:`Negative Effect <effect>` is 6 to 10, you lose 5 HP and pass out **(G-LOC)** [#]_ for [Effect/2] minutes.
   - If the :hoverxref:`Negative Effect <effect>` is 11 or more, you lose 10 HP and gain the ``Cerebral Hypoxia (Severe, -5)`` Condition for [Effect] minutes. 

.. [#] For example, if exposed to *4x your native gravity*, the Level would be 4, thus the difficulty would be 10+4 = 14. 

.. [#] **G-LOC** stands for *G-Force Induced Loss-of-Conciousness*, originally used in aerospace engineering and piloting.

**High-G exposure** can leave lasting effects in the form of more permanent Conditions (like bruising, muscle pain, or even bone fractures) at GM discretion, using the amount of HP lost or Conditions gained as a guidance. These effects can only be partially countered with these two methods:

- **Crash Couch**: These are specialized implements that resemble a mixture of a bean bag and a pilot seat. They are usually equipped in military vessels or spacecraft that are expected to do High-G maneuvers. They have a cushiony viscoelastic surface and an ergonomic build that softens your body from the high forces in an active fashion, with special gyroscope sensors.

  - While seated in a Crash Couch during High-G exposure, consider the effects suffered (both **long period** and **short burst** effects) to be one level lower in the previous table.

- **G-Juice**: Pilots or passengers that expect High-G exposure can inject hypodermic needle implements in their arm or neck veins. These are connected with tubes to a G-Juice dispenser [#]_, that pours this substance into the body to mitigate the discomforts of exposure to High-G. The apparatus can be connected to an expanded health monitoring system that can check the user’s vitals and administer the G-Juice as needed.

  - While connected to a G-Juice dispenser during High-G exposure, ignore the effects of the Conditions gained from High-G. You still lose HP as normal.

.. [#] G-Juice can also be injected with a regular needle from a standard vial, but the dose tends to be minimal, and its effect can last 10~30 minutes tops.

.. admonition:: Water-Tank Treatment

   Alternatively, if on a true gravity well, a person accustomed to a very low gravity (that is suffering from the higher gravity of the planet or moon they are on) can be submitted to a water-tank treatment. They are placed in a literal tank of water or similar liquid, with a respirator and/or a wetsuit. Floating in that liquid will mitigate considerably the effects of High-G exposure for them (in game terms, they ignore the effects of High-G while they are inside the tank).
 
Pressure and Atmosphere
-----------------------

.. figure:: /_static/images/rpg-image-18.jpg

   art © `Maciej Rebisz <https://mac.artstation.com/>`_

For a human body to function, there’s also the need for the right pressure and atmospheric composition.

What’s known as “breathable air” on Earth is usually composed of 75% Nitrogen, 24% Oxygen and other gasses. In space, the composition may vary slightly (depending on pressure, helium might be added to the mix, or oxygen levels could be increased).

Most stations and habitats that have hydroponic farms must also closely control their CO₂ levels, in order to guarantee proper plant growth (and to sustain a good cycle of 0₂ - C0₂ exchange).

Running out of oxygen
~~~~~~~~~~~~~~~~~~~~~

One of the dangers humans face when in space is oxygen deprivation. This might be caused by lots of reasons, like air recycler malfunctions, atmo mix going bad, oxygen supply running out, etc. When this happens but there is no pressure loss, it might be difficult to tell if air is running out or is just stuffy. The time it takes for oxygen to run out depends on many factors like volume of the environment, amount of people breathing it, etc, so the exact duration is left to GM discretion. When the time finally comes, a human can suffer the following effects:

.. csv-table:: Losing Oxygen
   :widths: 20, 80

   "1 Hour of Oxygen left", "Air is hard to breathe. Someone with an appropriate Skill might be allowed a roll to notice."
   "30 minutes of Oxygen left", "It’s getting hard not to hyperventilate. Everyone affected gains the ``Hard to breathe (Mild, -1)`` Condition, and loses 1 HP per minute."
   "5 minutes of Oxygen left", "Everyone can notice the first telltales of asphyxiation. Everyone affected gains the ``Asphyxiating (Moderate, -3)`` Condition, and loses 3 HP per minute."
   "All Oxygen gone", "Everyone automatically passes out. They lose 5 HP per minute until dead."

Losing pressure
~~~~~~~~~~~~~~~

.. figure:: /_static/images/rpg-image-22.jpg

   art © `Graham Gazzard <https://www.artstation.com/artwork/nQJN96>`_

Even with the right mix of gasses available, there has to be enough pressure in order to breathe. And that’s not even taking into account the myriad of problems caused to the human body in high or low pressure environments (especially if the change is abrupt!).

Regular pressure used in most space habitats is 1 bar. Pressure loss can occur at the environment level or at the personal level (your vac-suit). It might happen because the habitat or vessel hull/structure was somehow punctured or exposed to vacuum. In the case of a space-suit, a gash or perforation might do it.

**For every 2 cm of hole, you will lose 10 m³ of atmo each 10 seconds**. Keep in mind that small, room-sized modules have a volume of 30 m³, medium ones range from 50 m³ to 150 m³. Larger stations are usually divided in sections by “pressure doors” or hatches, with pressure sensors that automatically seal whatever module that is below ¾ atmo.

.. epigraph:: Depressurization Example

   *Someone was stupid enough to fire a gun inside a pressurized module (with a volume of 100m³) and puncture its hull. A 2 cm hole is punched through the thin wall. This means that the compartment will lose 10 m³ of air in the first 10 seconds. 30 seconds later, when the total air is down to 70m³ (below ¾ total), the pressure door automatically closes to avoid depressurization in the rest of the vessel. If noone patches the hole, the compartment will be fully depressurized in a total of 1 minute and 40 seconds (100 seconds).*

**Space-suits** have much less air volume circulating inside, but they also compensate by operating at much lower pressures (0.3 bar) and higher oxygen concentrations. Although most vac-suits have automated systems that increase oxygen output and sound alarms if they detect pressure loss, if the astronaut doesn’t plug or at least quickly cover the fissure, they will most likely fall unconscious in 10 seconds (see the effects of *Zero Pressure* in the :hoverxref:`Effects of Pressure Loss <effectsofpressureloss>` table).

Patching holes
^^^^^^^^^^^^^^

Most spacers have at hand a bunch of life-saving **Slap Patches**, which are folded circles of sticky plastic with a diameter of 15 to 30 cm. Just peel the backing away and adhere the patch to any hole. Of course, in an emergency, anything that can seal a puncture can be used. Most flat implements will be held in place by pressure alone. For longer-term solutions, soldering a plasteel slab or attaching a carbon-fiber mesh will do the trick.

.. _effectsofpressureloss:

.. container:: effectsofpressureloss

   .. csv-table:: Effects of Pressure Loss
      :widths: 20, 80

      "¾ of Normal Pressure", "No apparent effects other than eardrums popping. Anyone not accustomed to living/working in space will automatically lose 1 HP and do an :hoverxref:`Instinct Check <instinct-checks>`. Habitats or vessels that have pressure sensors will detect pressure loss and attempt to close hatches, if available."
      "½ of Normal Pressure", "The air in the area is becoming hard to breathe. Anyone without a respirator or vac-suit gains the ``Hard to breathe (Mild, -1)`` Condition."
      "¼ of Normal Pressure", "The oxygen in the volume is less than required to remain conscious. If the depressurization was abrupt, everyone exposed gains the ``Asphyxiating (Moderate, -3)`` Condition. If it took a while, everyone affected automatically falls unconscious. Additionally, characters affected will lose 5 HP per minute, and gain the ``The Bends (Moderate, -3)`` Condition, as nitrogen boils out of the blood, until *Zero Pressure* is reached."
      "Zero Pressure", "The compartment is airless and in a vacuum. Anyone exposed begins to suffer extreme pain; huge bruises begin to form all over their bodies, their blood boils, surface capillaries begin to burst, their eardrums rupture, and their noses and ears bleed. They gain ``The Bends (Moderate, -3)`` Condition if they didn’t already have it. Additionally, each character loses 1 HP per second until dead."
    
   When someone is *“spaced”* (thrown out of an airlock without a vac-suit), they immediately begin to suffer the effects of **Zero Pressure**.

   If someone somehow survives depressurization and returns to a living environment in time, the Conditions turn into all the nasty consequences they suffered (bruising, burns, hemorrhage, deafness, etc), which take months and special treatment to recover from.

Radiation
---------

.. figure:: /_static/images/rpg-image-19.jpg

   art © `Maciej Rebisz <https://mac.artstation.com/>`_

Radiation consists of invisible, tiny atomic particles which break havoc when passing through the human body. Radiation damages DNA inside cells, giving rise to cancer in the body or even killing it in a nasty way.

Radiation is of utmost importance to spacers because they are not protected by a huge magnetic field and a dense atmosphere like earthers do. Its dosage is usually measured in **Sieverts** (Sv) or **milliSieverts** (mSv). As the name suggests, 1000 mSv equals 1 Sv.

Characters that receive a dose of Radiation of 1+ Sv in a short time span automatically [#]_ lose 1 HP per Sv received, plus any effects detailed on the *Radiation Effects* table.

.. [#] it could actually take a few minutes for the health loss to kick in, at GM discretion.

Radiation effects
~~~~~~~~~~~~~~~~~

Players must tally each specific amount of Sv their characters gain. They will acquire :hoverxref:`Conditions <conditions>` on certain occasions, related to the amount of radiation they have been exposed to.

.. csv-table:: Radiation Effects
   :header: "Sv Acquired", "Radiation Sickness Effects"
   :widths: 20, 80

   "0 ~ 500 mSv", "None ― somewhat safe radiation levels"
   "500 mSv ~ 1 Sv", "Gain the ``Cell Mutations (permanent, -0)`` Condition. It only affects your offspring, increasing their chance of genetic disorders. 
   
   If received in a **short time span**, also gain the ``Mild Nausea (-1)`` Condition."
   "1 Sv", "Gain the ``Minor Cancer (permanent, -0)`` Condition. It’s early stage and can be treated by simple treatments (usually taking anti-cancer pills keeps it at bay). 
   
   If received in a **short time span**, also gain the ``Vomiting (Moderate, -3)`` Condition."
   "2 Sv", "Gain the ``Cataracts (Moderate, -3)`` Condition. You will gradually become blind, unless corrected via simple surgery. 
   
   If received in a **short time span**, also gain ``Fever and Headaches (Moderate, -3)``."
   "3 Sv", "Gain the ``Infertility Disorder (permanent, -0)`` Condition. Your chances of conception are reduced to 30%. If female, chances of spontaneous abortion are severely increased. 
   
   If received in a **short time span**, also gain the ``Hair loss (permanent, -0)`` Condition."
   "4 Sv", "Gain the ``Moderate Cancer (permanent, -0)`` Condition. Fortunately, medical science has advanced a lot, and these types of cancers are easily kept at bay with a monthly treatment session. You can mostly continue living a normal life if you maintain your medical schedule. 
   
   If received in a **short time span**, also gain ``Bloody Vomits (Severe, -5)``."
   "5 Sv", "Gain the ``Sterile (permanent, -0)`` Condition. Your chances of conception are nil, and there is no known treatment at this level of radiation poisoning. 

   If received in a **short time span**, also gain ``Internal Bleeding (Severe, -5)``."
   "6+ Sv", "Gain the ``Severe Cancer (permanent, -0)`` Condition. Even if caught at an early stage, this type of cancer requires regular weekly treatment sessions to avoid death. It might go into remission for a period of 6 months before inevitably coming back. If untreated, the character dies in 6 months. 
   
   If received in a **short time span**, also gain ``Skin Blistering (Severe, -5)``."

Sources of Radiation
~~~~~~~~~~~~~~~~~~~~

The 3 major sources of Radiation in space (or anywhere without a strong magnetosphere) are:

- **Cosmic** and **Background Radiation**
- **Nuclear power plants** and **Fusion Drives**
- **Solar Flares** and **Solar Storms**

Cosmic and Background Radiation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Cosmic rays** are clusters of high-energy particles that move through space at nearly the speed of light. They originate from the Sun, from outside of the Solar System in our own galaxy, and from distant galaxies. They are basically everywhere, like a constant invisible shower that you expose to whenever you are not in an underground or heavily-reinforced habitat.

Since **Background Radiation** is only dangerous if accumulated over long periods of time, GM and players should not concern themselves with immediate effects, but consult the following table for long-term exposure [#]_ (only apply immediate effects when a notorious amount of Sieverts is acquired, using the *Radiation Effects* table, above):

.. [#] This means the total exposure time of a spacer during their life or career. If the individual is mostly living in small space stations or spacecraft, then count the total time exposed. If, instead, they live or work mostly in underground habitats or ones with strong radiation shielding, only count the “time of service” they were exposed to Background Radiation.

.. csv-table:: Background Radiation Long-Term Exposure Time
   :header: "Total time exposed to Background Radiation", "Sieverts acquired"

   "1 month", "25 mSv"
   "6 months", "150 mSv"
   "1 year", "300 mSv"
   "2 years", "600 mSv"
   "5 years", "1.5 Sv"
   "10 years", "3 Sv"
   "20 years", "6 Sv"


Nuclear power plants and Fusion Drives
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Spacers are constantly near some sort of nuclear reactor, like those powering satellites or space stations, surface habitats, and spacecraft fusion drives. Any of those can fail at any time, and if there is an accident, they could expose nearby humans to nuclear radiation. When this happens, use the following table:

.. csv-table:: Nuclear Reactor Exposure
   :header: "Type or amount of exposure", "Sieverts acquired"

   "Far away / exposed to fallout", "100 mSv per minute"
   "Close by / behind some sort of protection", "500 mSv per minute"
   "Very close / inside reactor building or module", "1 Sv per minute"
   "Extremely close / exposed to the reactor core", "10 Sv per minute"

Solar Flares and Solar Storms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A **Solar Flare** is a deadly wave of radioactive particles ejected into a specific direction through space from the sun’s surface. They can disrupt communications, interrupt power sources, corrode solar panels, and give you extreme doses of radiation. During a Solar Flare there are few safe places to be, such as a planet with a magnetosphere like Earth, behind lots of shielding in a space station or in a vessel’s anti-rad chamber, or underground with several meters of rock over your head [#]_.

Solar Flares can be 500 Mm wide, although the average is a third of that size [#]_. 

.. [#] If behind partial cover (like not-so-thick shielding), reduce the Sv received by half.
.. [#] for reference, Jupiter’s diameter is 140 Mm.

Solar Flares are very rare, but there are warning devices all over the Solar System that can give at least two hours notice that one is building up. Most emergency channels and news outlets are very serious about distributing this information as fast as possible for spacers all over the system. **Solar Flares** usually last for 3 to 6 hours. **Solar Storms** are weaker versions that last longer (taking up to 10 days).

- A character fully exposed to a **Solar Flare** will receive 5 Sv immediately, plus 5 Sv every minute.
- For **Solar Storms**, exposure grants 500 mSv immediately and 500 mSv more each minute.

Temperature
-----------

.. figure:: /_static/images/rpg-image-20.jpg

   art © `Maciej Rebisz <https://www.artstation.com/mac>`_


Inside a Spaceship or Space Station, temperatures are usually kept warm enough to reduce its inhabitants’ metabolic load, but cool enough to avoid unnecessary sweating. This ideal temperature turns out to be somewhere between 18° and 24° C.

Heat in Space
~~~~~~~~~~~~~

The vacuum of space is usually at near absolute zero (0°K, or -273°C), but still, spaceships generate heat, and instead of freezing, they have the problem of overheating. How is this possible?

There are three primary methods of heat transfer: **conduction**, **convection**, and **radiation**.

- **Conduction** occurs when heat is transferred from one solid object to another through direct contact, like when your hand becomes burned if you touch a hot stove.
- **Convection** occurs when heat is transferred through a medium such as air or water. For example, you can cool down the temperature of your body by turning on a fan or jumping in a swimming pool. But this is not an option for spacecraft, because space is a vacuum and there is no medium to allow heat to be transferred away from the spacecraft.
- Finally, there is **radiation**―and this is really the only means of releasing heat in space. Radiation occurs when heat energy is emitted away from an object in the form of electromagnetic or thermal energy through waves of photons.

Spaceships and Space Stations make use of huge heat radiators that are usually deployed coplanar (in opposite sides), facing outwards, and they are commonly filled with tubes that circulate some sort of liquid that transfers heat out from the hotter parts of the craft. At the highest temperatures, these radiators glow in a dull red color.

.. figure:: /_static/images/rpg-image-23.jpg

   art © `Theo Bouvier <https://www.artstation.com/theo_bouvier>`_

There are other techniques to reduce heat generation and transfer: Ships and stations are usually painted white or in a silvery metallic coating, to reflect as much sunlight as possible. Another trick is to rotate the craft regularly to change the side that is being hit by sunlight, letting the other cool off while “in the shade”.

Waste Heat
^^^^^^^^^^

Any craft under normal operation will still have to get rid of some amount of waste heat (even the human body at rest generates heat!). Sunlight alone can increase the temperature of a vessel to 120°C in 10 minutes if not properly cooled.

During stress or moments of high consumption of energy (think under high burn with reactors at peak capacity, or when laser cannons are activated), any excess heat that the radiators cannot reject will start to build up on the craft itself, increasing the temperature of the hull and its interiors.

.. csv-table:: Heat Management
   :header: "Craft/Station Activity", "Craft/Station Temperature"

   "Moderate energy consumption
   
   (Normal Operations)", "18°~24° C 
   
   (baseline comfortable temperature)"
   "High energy consumption 
   
   (Reactor/thrusters at high capacity or active laser cannon)", "+10° C 
   
   (almost instant; reverts in 10 minutes after back to baseline consumption)"
   "Extreme energy consumption 
   
   (Reactor/thrusters at peak capacity AND active laser cannon(s))", "+20° C 
   
   (almost instant; reverts in 10 minutes after back to baseline consumption)"
   "Half of Heat Radiators damaged/offline", "+5° C per minute"
   "All Heat Radiators damaged/offline", "+10° C per minute"

Heat Sinks
^^^^^^^^^^

Some spaceships, specially those fitted for warfare, also use **Heat Sinks**. These are ejectable blocks of metal or some phase-changing material that absorbs heat (like a block of ice that is heated into steam).

When required, the vessel can eject said Heat Sink at once, **recovering -10° C**. A spaceship can carry as many Heat Sinks as needed, taking into account that to work properly each **weighs 1 Ton**.

Some advanced Heat Sinks are reusable; they have a very basic propelling system that “breaks” closeby and can be retrieved later, or even be redirected to “dock” back into their launching hardpoint. These are of cutting-edge military technology that is not available for public use.

.. admonition:: Temperature: CRITICAL

   If a craft reaches **CRITICAL TEMPERATURE LEVELS** (dangerous for life aboard), the crew can still do some things to slow it down or counteract it, like turning off non-critical systems and other high-consumption functions, moving/rotating away from sunlight, venting off hot propellant or other liquids/gases, ejecting Heat Sinks, and even cycling down the reactor. These are temporary fixes that might give them a few more minutes or even hours, but heat will continue building up until they repair or bring the radiators back online, at GM’s discretion.


Effects of temperature on the body
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table represents the effects of different temperatures on the human body and its consequences in game terms, assuming that the person is not properly protected/shielded.

.. csv-table:: Temperature Effects in the Human Body
   :widths: 20, 80

   "**Environmental Temperature**", "**Effects in the body** for *short exposure* (a few seconds up to a minute) or *long exposure* (a few minutes or more)."
   "Less than 15° C", "*Short exposure*: Gain ``Hypothermia (Moderate, -3)``; extreme shivering.

   *Long exposure*: Gain ``Frostbite (Severe, -5)`` and Immediately and for every hour of continuous exposure, lose 3 HP."
   "Less than 0° C", "*Short exposure*: very uncomfortable shivering and muscle cramps.

   *Long exposure*: Gain the ``Severe Hypothermia (-5)`` Condition."
   "0° ~ 10° C", "*Short exposure*: uncomfortable shivering or chills.

   *Long exposure*: Gain the ``Moderate Hypothermia (-3)`` Condition."
   "15° ~ 25° C", "Comfortable range for most individuals."
   "30° ~ 35° C", "The body begins sweating more to cool itself down.

   *Short exposure*: sweating, fatigue.

   *Long exposure*: Gain the ``Mild Dehydration (-1)`` Condition."
   "40° C", "Heat stress becomes significant.

   *Short exposure*: sweating, dizziness, confusion, fainting.

   *Long exposure*: Gain ``Moderate Dehydration (-3)``, and Immediately and for every hour of continuous exposure, lose 3 HP."
   "45° C", "Risk of heat exhaustion or heat stroke increases significantly. Proteins in the body begin denaturing, nerve impulses slow down, and organ function may be compromised.

   *Short exposure*: sweating, nausea, dizziness, confusion, fainting.

   *Long exposure*: Gain ``Heat Stroke (Severe, -5)`` and Immediately and for every hour of continuous exposure, lose 5 HP."
   "50° C or more", "The body loses its ability to cool itself effectively. Sweating becomes insufficient, leading to a dangerous rise in core temperature. Heat stroke may cause severe damage to organs such as the brain, heart, kidneys, and liver.

   *Short exposure*: sweating, nausea, dizziness, confusion, fainting.
   *Long exposure*: Gain ``Heat Stroke (Severe, -5)`` and Immediately and for every hour of continuous exposure, lose 10 HP."