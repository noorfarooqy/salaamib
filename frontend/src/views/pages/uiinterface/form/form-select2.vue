<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="page-header">
        <div class="content-page-header">
          <h5>Form Select2</h5>
        </div>
      </div>
      <div class="row">
        <div class="col-md-6">
          <!-- Basic -->
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Basic</h5>
            </div>
            <div class="card-body card-buttons">
              <div class="row">
                <div class="col-md-12">
                  <p>
                    Use select2() function on select element to convert it to Select 2.
                  </p>
                  <vue-select :options="orange" id="orange" placeholder="orange" />
                </div>
              </div>
            </div>
          </div>
          <!-- /Basic -->

          <!-- Nested -->
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Nested</h5>
            </div>
            <div class="card-body card-buttons">
              <div class="row">
                <div class="col-md-12">
                  <p>Add options inside the optgroups to for group options.</p>
                  <select class="form-control nested">
                    <optgroup label="Group1">
                      <option selected="selected">orange</option>
                      <option>white</option>
                      <option>purple</option>
                    </optgroup>
                    <optgroup label="Group2">
                      <option>purple</option>
                      <option>orange</option>
                      <option>white</option>
                    </optgroup>
                    <optgroup label="Group3">
                      <option>white</option>
                      <option>purple</option>
                      <option>orange</option>
                    </optgroup>
                  </select>
                </div>
              </div>
            </div>
          </div>
          <!-- /Nested -->

          <!-- Placeholder -->
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Placeholder</h5>
            </div>
            <div class="card-body card-buttons">
              <div class="row">
                <div class="col-md-12">
                  <p>Apply Placeholder by setting option placeholder option.</p>
                  <vue-select :options="Choose" id="choose" placeholder="Choose..." />
                </div>
              </div>
            </div>
          </div>
          <!-- /Placeholder -->

          <!-- Tagging with multi-value -->
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Tagging with multi-value select boxes</h5>
            </div>
            <div class="card-body card-buttons">
              <div class="row">
                <div class="col-md-12">
                  <p>Set tags: true to convert select 2 in Tag mode.</p>
                  <a-select v-model:value="selectedItems" mode="multiple" style="width: 100%"
                    :options="filteredOptions.map((item) => ({ value: item }))"></a-select>
                </div>
              </div>
            </div>
          </div>
          <!-- /Tagging with multi-value -->
        </div>

        <div class="col-md-6">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Small Select2</h5>
            </div>
            <div class="card-body card-buttons">
              <div class="row">
                <div class="col-md-12">
                  <p>Use data('select2') function to get container of select2.</p>
                  <vue-select :options="orange1" id="orange1" placeholder="orange" />
                </div>
              </div>
            </div>
          </div>

          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Disabling options</h5>
            </div>
            <div class="card-body card-buttons">
              <div class="row">
                <div class="col-md-12">
                  <p>Disable Select using disabled attribute.</p>
                  <vue-select :options="one" id="one" placeholder="First" />
                </div>
              </div>
            </div>
          </div>

          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Limiting the number of Tagging</h5>
            </div>
            <div class="card-body card-buttons">
              <div class="row">
                <div class="col-md-12">
                  <p>
                    Set maximumSelectionLength: 2 with tags: true to limit selectin in
                    Tag mode.
                  </p>
                  <a-select v-model:value="selectedItems1" mode="multiple" style="width: 100%"
                    :options="filteredOptions1.map((item) => ({ value: item }))"></a-select>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { computed, ref } from "vue";
const OPTIONS = ["orange", "white", "purple"];
export default {
  data() {
    return {
      title: "Form Select2",
      orange: ["orange", "white", "purple"],
      orange1: ["orange", "white", "purple"],
      Choose: ["Choose...", "First", "Second", "Third", "Fourth", "Fifth"],
      one: ["First", "Second", "Third"],
    };
  },
  setup() {
    const selectedItems = ref([]);
    const filteredOptions = computed(() =>
      OPTIONS.filter((o) => !selectedItems.value.includes(o))
    );
    const selectedItems1 = ref([]);
    const filteredOptions1 = computed(() =>
      OPTIONS.filter((o) => !selectedItems1.value.includes(o))
    );
    return {
      selectedItems,
      filteredOptions,
      selectedItems1,
      filteredOptions1,
    };
  },
  name: "form-select2",
};
</script>