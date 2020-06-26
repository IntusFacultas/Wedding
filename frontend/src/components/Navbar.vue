<template>
  <raw-navbar class="navbar" flavor="Navbar" :title="title" :fixed="true">
    <navbar-content></navbar-content>
    <navbar-content>
      <navbar-item flavor="Navbar">
        <a href="#details">Details</a>
      </navbar-item>
      <navbar-item flavor="Navbar">
        <a href="#">Registry</a>
      </navbar-item>
      <navbar-item flavor="Navbar">
        <a href="#">FAQ</a>
      </navbar-item>
      <n-button class="navbar__rsvpbutton" flavor="Secondary" :outline="true">RSVP</n-button>
    </navbar-content>
  </raw-navbar>
</template>

<script>
import RawNavbar from "@IntusFacultas/raw-navbar";
import { NavbarContent, NavbarItem } from "@IntusFacultas/navbar";
import Logo from "../assets/Wedding Logo.svg";
import { NButton } from "@IntusFacultas/button";
export const Navbar = {
  components: {
    RawNavbar,
    NavbarContent,
    NavbarItem,
    NButton
  },
  data() {
    return {
      title: {
        html: `<img class="navbar__brandicon" src="${process.env.VUE_APP_STATIC_URL}${Logo}" alt="April and Pedro's initials"></img>`,
        url: "#",
        text: ""
      }
    };
  }
};
export default Navbar;
</script>

<style>
.navbar {
  border-bottom: 1px solid #444;
}
.navbar__rsvpbutton {
  color: initial !important;
  height: 40px;
  text-align: center;
  width: 70px;

  margin: auto 5px;
}
@media screen and (max-width: 460px) {
  .navbar__rsvpbutton {
    line-height: 1.5;
  }
}
.navbar__rsvpbutton:hover {
  color: white !important;
  height: 40px;
  margin: auto 5px;
}
.navbar__brandicon {
  height: 35px;
}
</style>