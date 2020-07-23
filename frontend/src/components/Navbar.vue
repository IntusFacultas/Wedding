<template>
  <raw-navbar class="navbar" flavor="Navbar" :title="title" :fixed="true">
    <navbar-content></navbar-content>
    <navbar-content>
      <navbar-item>
        <a href="#details">Details</a>
      </navbar-item>
      <navbar-item>
        <a href="#">Registry</a>
      </navbar-item>
      <navbar-item>
        <a href="#">FAQ</a>
      </navbar-item>
      <navbar-item class="navbar__rsvpbuttoncontainer">
        <n-button class="navbar__rsvpbutton" flavor="Secondary" :outline="true">RSVP</n-button>
      </navbar-item>
    </navbar-content>
  </raw-navbar>
</template>

<script>
import RawNavbar from "@IntusFacultas/raw-navbar/src/RawNavbar";
import { NavbarContent, NavbarItem } from "@IntusFacultas/navbar/src/Navbar";
import Logo from "../assets/Wedding Logo.svg";
import { NButton } from "@IntusFacultas/button";
export const Navbar = {
  components: {
    RawNavbar,
    NavbarContent,
    NavbarItem,
    NButton,
  },
  data() {
    return {
      title: {
        html: `<img class="navbar__brandicon" src="${process.env.VUE_APP_STATIC_URL}${Logo}" alt="April and Pedro's initials"></img>`,
        url: "#",
        text: "",
      },
    };
  },
};
export default Navbar;
</script>

<style>
.navbar {
  border-bottom: 1px solid #444;
  opacity: 0.9;
}
.navbar__rsvpbuttoncontainer:hover {
  background-color: initial;
}
.navbar__rsvpbutton {
  color: initial !important;
  height: 40px;
  text-align: center;
  /* width: 70px; */

  /* margin: 5px 5px; */
}
@media screen and (max-width: 460px) {
  .navbar__rsvpbutton {
    line-height: 1.5;
    display: block;
    /* width: 100%; */
    /* margin: 5px 0; */
  }
}
.navbar__rsvpbutton:hover {
  color: white !important;
  height: 40px;
}
.navbar-brand {
  display: flex;
  height: 50px;
  align-items: center;
}
.nav-button {
  background-color: white !important;
}
.nav-button:hover {
  background-color: #f0f0f0 !important;
}
.navbar__brandicon {
  height: 35px;
}
</style>
