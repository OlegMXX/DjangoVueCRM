<template>
  <div>
    <Navbar/>

    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading }">
      <div class="lds-dual-ring" v-bind:class="{'is-loading': $store.state.isLoading }"></div>
    </div>

    <section class="section">
      <router-view/>
    </section>
</div>
  
</template>

<script>
    import axios from 'axios';
    import Navbar from '@/components/layout/Navbar'
    
    export default {
      name: 'App',
      components: {
        Navbar
      },
      beforeCreate() {
        this.$store.commit('initializeStore')

        if (this.$store.state.token) {
          axios.defaults.headers.common['Authorization'] = "Token " + this.$store.state.token
        } else {
          axios.defaults.headers.common['Authorization'] = ""
        }

        if (!this.$store.state.team.id) {
          this.$router.push('/dashboard/add-team')
        }
      },
    }

</script>

<style lang="scss">
@import '../node_modules/bulma';

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 0px;

  &.is-loading {
    visibility: visible;
    height: 0px;
  }
}



.lds-dual-ring:after {
  content: " ";
  visibility: hidden;
  display: block;
  width: 64px;
  height: 0px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;

  &.is-loading {
    visibility: visible;
    height: 0px;
  }

  
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.lds-loading-bar {
  visibility: hidden;
  height: 0px;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}

</style>
