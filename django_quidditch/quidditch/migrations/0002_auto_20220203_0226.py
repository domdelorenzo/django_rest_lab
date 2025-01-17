# Generated by Django 4.0.2 on 2022-02-03 02:26

from django.db import migrations
def seed(apps, schema_editor):
    Team = apps.get_model('quidditch', 'Team')
    Player = apps.get_model('quidditch', 'Player')
    thats_so_ravenclaw = Team(name="That\'s So Ravenclaw", location="Pateley Bridge", conference="Midsouth National", wins="18", losses="2" )
    snapes_on_a_plane = Team(name="Snapes on a Plane", location="North Seaford", conference="Midsouth National", wins="22", losses="0" )
    snitches_get_stitches = Team(name="Snitches Get Stiches", location="Bromsgrove", conference="Midsouth National", wins="10", losses="10" )
    ninetynine_problems = Team(name="99 Problems But a Snitch Ain\'t One", location="East Wirksworth", conference="Midsouth National", wins="2", losses="18" )
    gryffinpuffs = Team(name="Gryffinpuffs", location="Okehampton", conference="East Underground Regional", wins="5", losses="15" )
    puddlemere_united = Team(name="Puddlemere United", location="South Withernsea", conference="East Underground Regional", wins="5", losses="7" )
    granger_zone = Team(name="Granger Zone", location="East Treebans", conference="East Underground Regional", wins="14", losses="4" )
    thats_so_ravenclaw.save()
    snapes_on_a_plane.save()
    snitches_get_stitches.save()
    ninetynine_problems.save()
    gryffinpuffs.save()
    puddlemere_united.save()
    granger_zone.save()

    Player(team=thats_so_ravenclaw, name="Matthew Entwhistle", position="Chaser", age="14", injured="False").save()
    Player(team=thats_so_ravenclaw, name="Garrick Glossop", position="Beater", age="22", injured="False").save()
    Player(team=thats_so_ravenclaw, name="Eugene Truman", position="Keeper", age="36", injured="False").save()
    Player(team=snapes_on_a_plane, name="Yuvraj Abercrombie", position="Chaser", age="23", injured="False").save()
    Player(team=snapes_on_a_plane, name="David Kadam", position="Seeker", age="76", injured="False").save()
    Player(team=snapes_on_a_plane, name="Isabella Bagby", position="Keeper", age="7", injured="False").save()
    Player(team=snitches_get_stitches, name="Eglantine Frimley", position="Chaser", age="36", injured="False").save()
    Player(team=snitches_get_stitches, name="Leanne Madley", position="Seeker", age="66", injured="False").save()
    Player(team=snitches_get_stitches, name="George Prewett", position="Keeper", age="45", injured="False").save()
    Player(team=ninetynine_problems, name="Avery Pershore", position="Chaser", age="43", injured="False").save()
    Player(team=ninetynine_problems, name="Avery Dedworth", position="Seeker", age="22", injured="False").save()
    Player(team=ninetynine_problems, name="Rohit Puffett", position="Keeper", age="33", injured="False").save()
    Player(team=gryffinpuffs, name="Helga Hopkins", position="Chaser", age="22", injured="False").save()
    Player(team=gryffinpuffs, name="Owen Pickering", position="Seeker", age="11", injured="False").save()
    Player(team=gryffinpuffs, name="Millicent Gupta", position="Keeper", age="67", injured="False").save()
    Player(team=puddlemere_united, name="Andre Cooper", position="Chaser", age="28", injured="False").save()
    Player(team=puddlemere_united, name="Anthony Copplestone", position="Seeker", age="21", injured="False").save()
    Player(team=puddlemere_united, name="Miyuki Bampton", position="Keeper", age="19", injured="False").save()
    Player(team=granger_zone, name="Martine Madley", position="Chaser", age="86", injured="False").save()
    Player(team=granger_zone, name="Chauncy Knighton", position="Seeker", age="43", injured="False").save()
    Player(team=granger_zone, name="Danny Midhurst", position="Keeper", age="33", injured="False").save()
    Player(team=granger_zone, name="Elizabeth Stradbroke", position="Chaser", age="27", injured="False").save()
    Player(team=snapes_on_a_plane, name="Eleanor Applebee", position="Seeker", age="22", injured="False").save()
    Player(team=ninetynine_problems, name="Terry Warren", position="Keeper", age="16", injured="True").save()
    Player(team=gryffinpuffs, name="Barnaby Lee", position="Chaser", age="12", injured="False").save()
    Player(team=puddlemere_united, name="Tomoko Fronsac", position="Seeker", age="87", injured="True").save()
    Player(team=thats_so_ravenclaw, name="Manoj Diggory", position="Keeper", age="22", injured="False").save()


def fallow(apps, schema_editor):
    Team = apps.get_model('quidditch', 'Team')
    Player = apps.get_model('quidditch', 'Player')
    Team.objects.all().delete()
    Player.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('quidditch', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, fallow)
    ]


