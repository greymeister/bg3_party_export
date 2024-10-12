-- Run with initial avatar
_Purge=_C().ServerCharacter.Template.Name .. "_" .. GetHostCharacter()

-- Run after Import
-- Source - https://old.reddit.com/r/BaldursGate3/comments/15qb8lu/guide_removing_custom_multiplayer_party_members/
MakeNPC(_Purge)
SetFaction(_Purge, "NPC_cfb709b3-220f-9682-bcfb-6f0d8837462e")
SetHasDialog(_Purge, 0)
SetOnStage(_Purge, 0)
Osi.DB_Players:Delete(_Purge)
Osi.DB_Avatars:Delete(_Purge)
Osi.DB_PartOfTheTeam:Delete(_Purge)
Osi.DB_IsOrWasInParty:Delete(_Purge)
Osi.DB_GLO_PartyMembers_InPartyDialog:Delete(_Purge, "NULL_00000000-0000-0000-0000-000000000000")
Osi.PROC_RemoveAllPolymorphs(_Purge)
Osi.PROC_RemoveAllDialogEntriesForSpeaker(_Purge)
SetImmortal(_Purge, 0)
Die(_Purge, 0, "NULL_00000000-0000-0000-0000-000000000000", 0, 0)
Osi.PROC_CheckPartyFull()