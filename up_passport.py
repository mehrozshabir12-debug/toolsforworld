"""Unique content: passport and visa photo presets."""

P = {}

P["us-passport-photo"] = ('''<h2>Making a 2 × 2 inch photo at home</h2>
<p>Stand about four feet from the camera with a white wall or a white sheet behind you, and ask someone else to take the picture at eye level rather than holding the phone yourself. Selfies are taken at arm's length, which makes the nose look larger and the ears smaller, and the State Department asks for a natural, undistorted face. Face a window for soft daylight so there are no shadows behind your head.</p>
<p>After you choose the photo, drag and zoom until your chin sits on the lower guide and the top of your hair touches the upper one. The square crop is saved at 600 × 600 pixels, which is also the smallest size the DS-160 visa form accepts.</p>
<h2>Printing the 4 × 6 sheet in the US</h2>
<p>The sheet holds two 2 × 2 inch photos side by side on a standard 4 × 6 inch print, which pharmacy and supermarket photo counters print for well under a dollar. Order it as a normal photo print, choose "no borders" or "original size", and make sure the kiosk doesn't apply "fit to page", which would shrink the photos. Measure one with a ruler: it should be exactly 2 inches on each side.</p>
<p>Applying with form DS-11 or DS-82? Attach the photo exactly the way the form's instructions describe, and keep it flat: a bent or scratched photo can be rejected.</p>''',
[("Can I smile in a US passport photo?", "A natural smile with your mouth closed is fine, or a neutral expression. Wide grins that show teeth and exaggerated faces are usually rejected."),
 ("Can I wear a hat or head covering?", "Not a hat. A head covering worn every day for religious reasons is allowed with a signed statement, or a medical one with a doctor's note, as long as your full face is visible.")])

P["uk-passport-photo"] = ('''<h2>Online or paper application?</h2>
<p>Most British passports are now applied for online. The online service asks for a <b>digital</b> photo, and you can take it on a phone at home: a friend photographs you against a plain cream or light grey wall, and you upload the full-size picture. The service checks it and crops it for you, so don't upload the small 35 × 45 mm print crop made here; upload the original photo instead.</p>
<p>The <b>printed</b> 35 × 45 mm photo is for paper forms, which some people still use, for example when applying from certain countries abroad or when a paper form was posted to them. Paper applications need two identical prints, and one is signed on the back by a countersignatory when the form asks for it.</p>
<h2>Getting the print right</h2>
<ul><li>Print the 4 × 6 sheet at a photo shop or kiosk on photo paper, at actual size.</li><li>Check the head height with a ruler: 29–34 mm from chin to the top of the head.</li><li>Cut cleanly along the guides with a ruler and a sharp blade, so both photos are exactly the same size.</li><li>Don't write on the front, and if a countersignatory signs the back, ask them to use a pen that won't smudge onto the other photo.</li></ul>''',
[("Do UK passport photos need to be taken in the last month?", "Yes. GOV.UK asks for a photo taken within the last month, which is stricter than many countries that allow 6 months."),
 ("Can children's photos be taken at home?", "Yes. Babies under one don't need to have their eyes open, and young children can be photographed lying on a plain sheet, as long as no hands or toys are visible.")])

P["canada-passport-photo"] = ('''<h2>Why Canada is different</h2>
<p>Canada is one of the few countries that doesn't accept home-made passport photos. The photographer must print the studio's name, address and the date the photo was taken on the back of one print, and, for a first passport, your guarantor also signs it. So this preset can't replace a photo studio for a Canadian passport, and we'd rather tell you that than have your application returned.</p>
<h2>What you can use it for</h2>
<ul><li><b>Practice:</b> see how the 50 × 70 mm frame looks with your hairstyle, glasses off, before you visit the studio, so the first shot is right.</li><li><b>Other Canadian forms</b> that ask for a passport-style photo but not a studio stamp, such as some membership, school or workplace ID cards. Check the form first.</li><li><b>Size check:</b> 50 × 70 mm is a tall rectangle. If someone hands you a photo for a Canadian application that is closer to square, it's probably the wrong size.</li></ul>
<p>Immigration documents from IRCC, such as permanent resident cards and some visas, have their own photo specifications. Each application guide lists the size it wants, and some of them accept 35 × 45 mm instead.</p>''',
[("Can I use a home-printed photo to renew a Canadian passport online?", "No. Canadian passport photos, including those used for renewals, must come from a commercial photographer, who adds the studio details and date."),
 ("What size is a Canadian passport photo in inches?", "50 × 70 mm is about 1.97 × 2.76 inches. It is taller than the 2 × 2 inch US photo, so the two can't be swapped.")])

P["australia-passport-photo"] = ('''<h2>No glasses, and how the print must be made</h2>
<p>The Australian Passport Office asks you to take glasses off for the photo, unless you can't remove them for medical reasons; needing glasses to see isn't one of those reasons. It also asks for a good colour print on glossy photo paper of at least 200 gsm made by dye sublimation, which is how most photo kiosks and pharmacy photo counters print. A home inkjet print on ordinary paper is not accepted.</p>
<p>So the realistic way to use this page is: take the photo at home, frame it here, download the 4 × 6 sheet and print it at a photo kiosk. Measure before you leave the shop. The photo should be 35 mm wide and 45 mm high, and your face from chin to crown 32–36 mm.</p>
<h2>Applying from Perth, Sydney or overseas</h2>
<p>Inside Australia you can lodge an application at a participating post office, and many of them can also take the photo for you. Abroad, Australian embassies and consulates follow the same rules, but some ask for the photo to be taken at a local studio that knows the requirements. Each embassy lists what it wants on its passport page.</p>
<p>For a first passport, a guarantor who has known you for at least 12 months usually signs the back of one photo. The application form explains when this is needed.</p>''',
[("Can I wear glasses in an Australian passport photo?", "No, unless you can't remove them for a medical reason. In that case the frames must not cover your eyes and the lenses must not reflect light."),
 ("How old can the photo be?", "Less than 6 months old, and it must still look like you now.")])

P["india-passport-photo"] = ('''<h2>Where Indians actually need a printed photo</h2>
<p>If you book an appointment at a Passport Seva Kendra or a Post Office Passport Seva Kendra, the photo is taken at the counter with a camera, so you don't bring one. Printed 35 × 45 mm photos are mostly needed for other things: paper forms such as college admissions, bank account opening and many state government applications.</p>
<h2>Photos for Indian forms filled online</h2>
<p>Exam and job portals in India, such as state recruitment boards and university portals, usually ask for a digital photo with both a pixel size and a KB range, for example 20–50 KB. Make the face crop here with the single-photo download, then bring it into range with <a href="../compress-image-to-50kb/">Compress Image to 50 KB</a> or <a href="../compress-image-to-20kb/">to 20 KB</a>. Read the notice for the exact limits, because they differ from portal to portal and are checked automatically.</p>
<p>White background, dark clothes and both ears visible is the safe combination for almost every Indian form, including those that don't spell out the rules.</p>''',
[("Is 35 × 45 mm the same as 3.5 × 4.5 cm?", "Yes. It's the same size, written in centimetres instead of millimetres, and it's the most common photo size on Indian forms."),
 ("Do I need to carry a photo to the Passport Seva Kendra?", "No. Your photo is taken at the PSK during the appointment. Bring your documents and the appointment receipt instead.")])

P["schengen-visa-photo"] = ('''<h2>One photo for 29 countries</h2>
<p>Whether you're applying for France, Germany, Italy, Spain, the Netherlands or any other Schengen member, the visa sticker uses the same biometric photo: 35 × 45 mm, a light, plain background and a face that fills about 70–80% of the height. Visa centres such as VFS Global and TLScontact will often take a photo at the appointment for a fee if yours is rejected, so getting it right in advance saves money.</p>
<h2>Common reasons visa centres reject photos</h2>
<ul><li><b>Head too small:</b> holiday-style photos where the face fills only half the frame. Zoom in until the chin and crown touch the guides.</li><li><b>Shadows on the background</b> from standing too close to the wall. Step half a metre forward.</li><li><b>Hair over the eyes or face</b>, or a fringe that hides the eyebrows.</li><li><b>Old photos:</b> the photo must be recent, usually no more than 6 months old, and look like you on the appointment day.</li><li><b>Prints from office paper</b>: use photo paper from a kiosk, not a laser print.</li></ul>
<p>Most applications need one photo glued or stapled to the form. Some embassies ask for two, so the 4 × 6 sheet gives you spares.</p>''',
[("Is a Schengen visa photo the same as a UK passport photo?", "The size is the same, 35 × 45 mm. The background differs slightly: the UK asks for cream or light grey, while Schengen countries usually accept white or light grey."),
 ("Do I need a photo for the online Schengen form?", "It depends on the country. Some online systems ask for an upload, others only want the printed photo at the appointment. The visa centre's checklist for your country says which.")])

P["china-visa-photo"] = ('''<h2>Printed and digital China visa photos</h2>
<p>China visa applications are filled in online and the same photo is used twice: uploaded in the online form and, at many visa centres, printed and brought to the appointment. The Chinese Visa Application Service Center asks for a digital photo in JPEG format no larger than 354 × 472 pixels and between 40 KB and 120 KB, taken in the last 6 months on a white or near-white background.</p>
<p>To make the digital version, download the single photo from this page, resize it to 354 × 472 with <a href="../resize-image/">Resize Image</a> (choose crop to fill), then check the size. If it's above 120 KB, use <a href="../compress-image/">Compress Image</a> with a target of about 100 KB. If it's under 40 KB, save it again at higher quality.</p>
<h2>Head size: the most common problem</h2>
<p>The 33 × 48 mm frame is narrower and taller than most passport photos, and the head must be 28–33 mm tall. People often leave too much space above the head. Line the top of your hair up with the upper guide and keep both ears and eyebrows visible. Remove glasses if they reflect light.</p>''',
[("What pixel size is a China visa photo?", "For the online form, no larger than 354 × 472 pixels, JPEG, 40–120 KB. The printed photo is 33 × 48 mm."),
 ("Can I use a US 2 × 2 photo for a China visa?", "No. China asks for 33 × 48 mm, which is narrower and taller. A square photo would be rejected or cropped badly.")])

P["pakistan-passport-photo"] = ('''<h2>When you need this photo</h2>
<p>At a regional passport office in Pakistan your picture is taken at the counter, so you don't bring one. A digital photo is needed when you apply through the <b>online passport</b> service, popular with overseas Pakistanis, and for many other forms: NADRA-related applications filled online, university and job portals, and visas for other countries that you apply to from Pakistan.</p>
<h2>Taking the photo at home in good light</h2>
<ul><li>Stand in front of a plain white wall during the day, facing a window, so the light is even on both sides of the face.</li><li>Keep the camera at eye level, about one and a half metres away, and zoom in later rather than coming close.</li><li>Wear dark, plain clothes, and avoid white shirts against the white background.</li><li>For a dupatta or hijab, keep the face fully visible from the chin to the forehead, with no shadow across the eyes.</li></ul>
<p>Download the single photo for the online form. If a portal asks for a size in KB, for example "under 100 KB", run it through <a href="../compress-image-to-100kb/">Compress Image to 100 KB</a> after cropping.</p>''',
[("What size is the photo for the Pakistan online passport?", "The online passport system asks for a digital photo, and this preset makes one at 350 × 467 pixels on a white background, matching the proportions it expects. Check the current upload rules on the DGI&P site before you apply."),
 ("Can I wear glasses?", "It's safest not to. Glasses often cause glare or shadows that get a photo rejected.")])
