<main>
    <div class="content-wrapper">
        <div class="date-wrapper">
            November 22, 2023
        </div>
        <div class="images-wrapper">
            <img src="/show_off_Nov_2023.png" alt='Devlog progess'/>
        </div>
        <div class="one-liner-wrapper">
            Damn this IK has hands, wait no it doesn’t…
        </div>
        <div class="meat-wrapper">
            <p class="paragraph-wrapper">
                I’ve hit a bit of a wall with the development of Show Off in a couple different ways. Technically I’ve been struggling with getting the IK to play nicely with the active ragdoll simulation. Ideally I would have all the bones being part of a ragdoll for the entire game, the player only controls the arms/hands, and if they fall then the arms and hands will also become part of the ragdoll. So a few weeks ago I got the inverse kinematics (IK) working with the hands tracking the mouse (as well as the direction of the head so it looks like the character is actually looking where the hands are), but when I turn on the ragdoll simulation with the built in method physical_bones_start_simulation(), all the fingers fall off! The Godot docs claim that this method can take in a list of bones, so I could try to exclude the IK portion of the character, but it hasn’t worked for me yet. Besides that the ragdoll works pretty good, I still need to tweak the joint constraints a little bit but I don’t think I want to spend too much time on this character as it won’t be the final model for the game.
            </p>
            <div></div>
            <p class="paragraph-wrapper">
                The other main thing that’s been hindering my progress is lack of motivation. I largely blame a certain game that I’ve been spending too much time on lately, but I think it goes a little deeper than that. The idea of making an entire game is daunting, and telling myself after a full day of work to sit down and “make a game” is a hard sell. I think in the future I’m going to instead focus on planning out small, specific tasks so that I can focus on just one thing at a time. I have a github projects page already, but have definitely been neglecting to update it. 
            </p>
            <div></div>
            <p class="paragraph-wrapper">
                Ideally next month I’ll have the character model able to actually grab onto the wall holds, let go, and pull themselves to the next one, regardless of the presence of hands or ragdoll capabilities. Hopefully in the future I can write one of these updates once at the beginning of each month, not a week before the end of the month :/.
            </p>
            <div></div>
        </div>
        <div class="divider-line"></div>
    </div>
    <div class="content-wrapper">
        <div class="date-wrapper">
            October 7, 2023
        </div>
        <div class="one-liner-wrapper">
            Lets see if this lasts past October
        </div>
        <div class="meat-wrapper">
            <p class="paragraph-wrapper">
                As I’ve been getting more interested in game development, the idea of creating dev logs has become increasingly appealing to me. They seem to be a great way to not only update your community about the development of your game, but always a perfect way to build that community over time while keeping yourself accountable. On the other hand, creating dev logs takes away from the already limited game dev time of someone who works a full time day job like myself. I’m always so impressed by indie game developers who consistently post high quality video dev logs. So to save time I plan on posting my dev blogs in text format here on my website.
            </p>
            <div></div>
            <p class="paragraph-wrapper">
                The primary goal of these dev logs is to keep myself accountable towards actually seeing this idea through to fruition, people reading them would be a bonus hahaha. I think a realistic goal would be to post at least one dev log a month. If things speed up and I’m feeling ambitious, there might be more but don’t get your hopes up. If you want to chat about anything at all, please reach out at 907riley@gmail.com!
            </p>
            <div></div>
        </div>
        <div class="divider-line"></div>
    </div>
    </main>

<style lang="scss">
    .date-wrapper {
        font-size: 2rem;
    }

    .one-liner-wrapper {
        font-size: .75rem;
        font-style: italic;
        opacity: 50%;
    }

    .meat-wrapper > div {
        height: 1rem;
    }

</style>