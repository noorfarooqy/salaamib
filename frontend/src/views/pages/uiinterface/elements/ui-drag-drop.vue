<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <element-breadcrumb :title="title" />
      <!-- Drag Card -->
      <draggable :list="list3" @change="log" class="row" id="card-drag-area">
        <div v-for="element in list3" :key="element.id" class="col-md-4 draggable">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">{{ element.name }}</h5>
            </div>
            <div class="card-body">
              <p>{{ element.para }}</p>
            </div>
          </div>
        </div>
      </draggable>
      <!-- /Drag Card -->

      <div class="row">
        <div class="col-md-12">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Basic List Group Sortable</h5>
            </div>
            <div class="card-body">
              <!-- Drag Card -->
              <ul class="list-group" id="basic-list-group">
                <draggable class="dragArea list-group w-full" :list="list2" @change="log">
                  <div v-for="element in list2" :key="element.id" class="list-group-item">
                    <div class="media-body">
                      <h5 class="mt-0">{{ element.name }}</h5>
                      <p>{{ element.para }}</p>
                    </div>
                  </div>
                </draggable>
              </ul>
              <!-- /Drag Card -->
            </div>
          </div>
        </div>
      </div>

      <div class="row">
        <!-- Drag Card -->
        <div class="col-md-12">
          <div class="card" id="dd-handle">
            <div class="card-header">
              <h5 class="card-title">Drag Handler</h5>
            </div>
            <div class="card-body">
              <div class="row">
                <div class="col-sm-6">
                  <h4 class="my-1">List One</h4>
                  <draggable class="dragArea list-group w-full" :list="list" @change="log">
                    <div class="list-group-item bg-gray-300 rounded-md" v-for="element in list" :key="element.name">
                      <span class="handle">+</span> {{ element.name }}
                    </div>
                  </draggable>
                </div>
                <div class="col-sm-6">
                  <h4 class="my-1">List Two</h4>
                  <draggable class="dragArea list-group w-full" :list="list1" @change="log">
                    <div class="list-group-item bg-gray-300 rounded-md" v-for="element in list1" :key="element.name">
                      <span class="handle">+</span> {{ element.name }}
                    </div>
                  </draggable>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- /Drag Card -->
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
import { VueDraggableNext } from "vue-draggable-next";
export default {
  components: {
    draggable: VueDraggableNext,
  },
  data() {
    return {
      title: "Drag & Drop",
      enabled: true,
      list: [
        { name: "Cras justo odio", id: 1 },
        { name: "Dapibus ac facilisis in", id: 2 },
        { name: "Morbi leo risus", id: 3 },
        { name: "Porta ac consectetur ac", id: 4 },
        { name: "Vestibulum at eros", id: 5 },
      ],
      list1: [
        { name: "Cras justo odio", id: 1 },
        { name: "Dapibus ac facilisis in", id: 2 },
        { name: "Morbi leo risus", id: 3 },
        { name: "Porta ac consectetur ac", id: 4 },
        { name: "Vestibulum at eros", id: 5 },
      ],
      list2: [
        {
          name: "Darren Elder",
          para:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod",
          id: 1,
        },
        {
          name: "Linda Ellis",
          para:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod",
          id: 2,
        },
        {
          name: "Toney Ritch",
          para:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod",
          id: 3,
        },
        {
          name: "Flora Jag",
          para:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod",
          id: 4,
        },
        {
          name: "Linda Marris",
          para:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod",
          id: 5,
        },
      ],
      list3: [
        {
          name: "Draggable Card 1",
          para:
            "Jelly beans sugar plum cheesecake cookie oat cake soufflé.Tootsie roll bonbon liquorice tiramisu pie powder.Donut sweet roll marzipan pastry cookie cake tootsie roll oat cake cookie.",
          id: 1,
        },
        {
          name: "Draggable Card 2",
          para:
            "Jelly beans sugar plum cheesecake cookie oat cake soufflé.Tootsie roll bonbon liquorice tiramisu pie powder.Donut sweet roll marzipan pastry cookie cake tootsie roll oat cake cookie.",
          id: 2,
        },
        {
          name: "Draggable Card 3",
          para:
            "Jelly beans sugar plum cheesecake cookie oat cake soufflé.Tootsie roll bonbon liquorice tiramisu pie powder.Donut sweet roll marzipan pastry cookie cake tootsie roll oat cake cookie.",
          id: 3,
        },
      ],
      dragging: false,
    };
  },
  methods: {
    log(event) {
      console.log(event);
    },
  },
};
</script>
