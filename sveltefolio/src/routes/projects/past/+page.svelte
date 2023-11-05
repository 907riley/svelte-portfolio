<div>
    <div class="content-wrapper">
        <div>
            <h1>Dunk</h1>
            <p class="worked-date-wrapper">August 2023</p>
        </div>
        <div class="images-wrapper">
            <img src='/dunk_main_menu.png' alt='dunk main menu scene'/>
            <img src='/dunk_gameplay.png' alt='dunk gameplay'/>
        </div>
        <a href='https://granitebouldergames.itch.io/dunk'>Itch.io</a>
        <ul class="description-list-wrapper">
            <li>
                Built with Godot for a two week long game jam with a friend.
            </li>
            <li>
                A first person 64 x 64 bit atmospheric horror game where the player plays as a diver stranded at the bottom of the ocean trying to fix their submarine.
            </li>
            <li>
                The player must collect parts scattered around the ocean floor while managing oxygen levels, flashlight battery, and being hunted by a creature.
            </li>
        </ul>
        <div class="divider-line"></div>
    </div>

    <div class="content-wrapper">
        <div>
            <h1>Job Hunt Tracker</h1>
            <p class="worked-date-wrapper">July 2023 - Present</p>
        </div>
        <div class="images-wrapper">
            <img src='/job_hunt_tracker_view.PNG' alt='job hunt tracker main view'/>
        </div>
        <div class="link-wrapper">
            <a href='https://application-tracker-vue.vercel.app/'>Website</a>
            <a href="https://github.com/907riley/application-tracker-vue">GitHub</a>
        </div>
        <ul class="description-list-wrapper">
            <li>
                Vue.js and Typescript application that allows users to store and manage all the information about the jobs they apply to, organized into job hunts.
            </li>
            <li>
                Uses supabase to handle CRUD along with user authentication via email.
            </li>
            <li>
                Frontend designed with Figma and tested with Vitest.
            </li>
        </ul>
        <div class="divider-line"></div>
    </div>

    <div class="content-wrapper">
        <div>
            <h1>Jig</h1>
            <p class="worked-date-wrapper">July 2023</p>
        </div>
        <div class="images-wrapper">
            <img src='/jig.gif' alt='jig logo'/>
            <img src='/jig_gameplay.png' alt='jig gameplay'/>
        </div>
        <a href='https://granitebouldergames.itch.io/jig'>Itch.io</a>
        <ul class="description-list-wrapper">
            <li>
                Built with Godot for a 48 hour game jame with a friend. Made a lot of the artwork with Aseprite.
            </li>
            <li>
                Created a pixel art rhythm fishing game that shuffled through random songs and difficulties.
            </li>
            <li>
                Players were awarded 1 of 10 possbile fish based on how they performed.
            </li>
        </ul>
        <div class="divider-line"></div>
    </div>

    <div class="content-wrapper">
        <div>
            <h1>Portfolio</h1>
            <p class="worked-date-wrapper">May 2023 - Present</p>
        </div>
        <div class="images-wrapper">
            <img id='svelte-logo-wrapper' src='/svelte_logo.png' alt='jig logo'/>
        </div>
        <p>This website</p>
        <ul class="description-list-wrapper">
            <li>
                I've gone through 3-4 redesigns of this website recently. Originally no js at all, then redesigned with js, then remade with Next.js, and then finally remade with Svelte.
            </li>
            <li>
                First time that I designed a website with a mobile first plan.
            </li>
        </ul>
        <div class="divider-line"></div>
    </div>


</div>

<style lang="scss">

    #svelte-logo-wrapper {
        width: 10rem;
    }

    .description-list-wrapper {
        list-style-type: circle;

        li {
            margin: 1rem 0rem 1rem 0rem;
        }
    }

    .images-wrapper {
        display: flex;
        flex-direction: row;
        gap: 1rem;

        img {
            // width: 100px;
            // height: 100px;
            min-width: 0;
            min-height: 0;
            flex: 1;
        }
    }

</style>